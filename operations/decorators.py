from functools import wraps
from django.http import HttpResponseForbidden
from django.template.loader import render_to_string

def role_required(allowed_roles):
    """
    Decorator to restrict access to users with specific roles.
    :param allowed_roles: List of allowed roles (e.g., ['adminstaff', 'employee']).
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                return HttpResponseForbidden("You are not authorized to view this page.")

            # Check if the user's role is in the allowed roles
            user_role = getattr(request.user.profile, 'role', None)  # Ensure 'profile' is related to the User
            if user_role not in allowed_roles:
                return HttpResponseForbidden(
                render_to_string('403.html', {"message": "You do not have access to view this page."})
            )

            # Proceed to the view if checks pass
            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator
