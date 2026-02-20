from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

from accounts.decorators import role_required
from accounts.models import UserProfile
from drives.models import Drive
from students.models import Student

from .models import Application


@role_required(UserProfile.Role.STUDENT)
def apply_drive(request, drive_id):
    student = get_object_or_404(Student, user=request.user)
    drive = get_object_or_404(Drive, id=drive_id)

    if not drive.is_student_eligible(student):
        messages.error(request, 'You are not eligible for this drive.')
        return redirect('students:dashboard')

    Application.objects.get_or_create(student=student, drive=drive)
    messages.success(request, 'Application submitted.')
    return redirect('students:dashboard')
