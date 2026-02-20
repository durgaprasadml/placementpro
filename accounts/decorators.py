from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect


def role_required(*allowed_roles):
    """Simple role guard that redirects users away from pages outside their role."""

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('accounts:login')
            role = getattr(getattr(request.user, 'profile', None), 'role', None)
            if role not in allowed_roles:
                messages.error(request, 'You are not authorized to access this page.')
                return redirect('accounts:role_redirect')
            return view_func(request, *args, **kwargs)

        return _wrapped

    return decorator
