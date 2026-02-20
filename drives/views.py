from django.shortcuts import redirect, render

from accounts.decorators import role_required
from accounts.models import UserProfile
from students.models import Student

from .forms import DriveForm
from .models import Drive


@role_required(UserProfile.Role.TPO)
def tpo_dashboard(request):
    if request.method == 'POST':
        form = DriveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drives:tpo_dashboard')
    else:
        form = DriveForm()

    drives = Drive.objects.all().order_by('-drive_date')
    students = Student.objects.select_related('user').all()

    # Build eligible student lists drive-wise for visibility in TPO panel.
    eligibility_map = []
    for drive in drives:
        eligible_students = [student for student in students if drive.is_student_eligible(student)]
        eligibility_map.append((drive, eligible_students))

    return render(
        request,
        'drives/tpo_dashboard.html',
        {
            'form': form,
            'eligibility_map': eligibility_map,
        },
    )
