from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import redirect, render
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from accounts.decorators import role_required
from accounts.models import UserProfile
from applications.models import Application
from drives.models import Drive

from .forms import StudentProfileForm
from .models import Student


@role_required(UserProfile.Role.STUDENT)
def dashboard(request):
    # Each user gets/edits one student profile record for simplicity.
    student, _ = Student.objects.get_or_create(
        user=request.user,
        defaults={
            'cgpa': 0,
            'branch': 'Not Set',
            'backlogs': 0,
            'skills': '',
            'projects': '',
        },
    )

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:dashboard')
    else:
        form = StudentProfileForm(instance=student)

    drives = Drive.objects.all().order_by('drive_date')
    eligible_drives = [drive for drive in drives if drive.is_student_eligible(student)]
    applications = Application.objects.filter(student=student).select_related('drive')

    return render(
        request,
        'students/dashboard.html',
        {
            'student': student,
            'form': form,
            'eligible_drives': eligible_drives,
            'applications': applications,
        },
    )


@role_required(UserProfile.Role.STUDENT)
def resume_pdf(request):
    student = Student.objects.filter(user=request.user).first()
    if not student:
        return redirect('students:dashboard')

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Simple ReportLab resume rendering.
    p.setFont('Helvetica-Bold', 16)
    p.drawString(72, 750, f'Resume - {request.user.get_full_name() or request.user.username}')
    p.setFont('Helvetica', 12)
    lines = [
        f'Branch: {student.branch}',
        f'CGPA: {student.cgpa}',
        f'Skills: {student.skills}',
        'Projects:',
    ]

    y = 720
    for line in lines:
        p.drawString(72, y, line)
        y -= 20

    for project_line in student.projects.split('\n'):
        p.drawString(90, y, f'- {project_line}')
        y -= 18

    p.showPage()
    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response
