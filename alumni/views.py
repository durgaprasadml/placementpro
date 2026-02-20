from django.shortcuts import redirect, render

from accounts.decorators import role_required
from accounts.models import UserProfile

from .forms import ReferralPostForm
from .models import AlumniProfile, ReferralPost


@role_required(UserProfile.Role.ALUMNI)
def dashboard(request):
    alumni, _ = AlumniProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ReferralPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.alumni = alumni
            post.save()
            return redirect('alumni:dashboard')
    else:
        form = ReferralPostForm()

    posts = ReferralPost.objects.filter(alumni=alumni).order_by('-created_at')
    return render(request, 'alumni/dashboard.html', {'form': form, 'posts': posts})


@role_required(UserProfile.Role.STUDENT, UserProfile.Role.TPO, UserProfile.Role.ALUMNI)
def referrals_feed(request):
    posts = ReferralPost.objects.select_related('alumni', 'alumni__user').order_by('-created_at')
    return render(request, 'alumni/referrals_feed.html', {'posts': posts})
