from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # URLs that don't require authentication
        self.exempt_urls = ['/admin/', '/accounts/login/', '/accounts/register/']
    
    def __call__(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            # Check if current path is in exempt URLs
            path = request.path
            if not any(path.startswith(exempt) for exempt in self.exempt_urls):
                # Redirect to login
                return redirect('accounts:login')
        
        response = self.get_response(request)
        return response
