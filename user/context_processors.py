from .models import UserProfile


def profile(request):
    if request.user.is_authenticated:
        return {'profile': UserProfile.objects.get(user=request.user)}