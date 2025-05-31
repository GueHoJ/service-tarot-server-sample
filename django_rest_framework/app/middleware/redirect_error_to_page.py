# middleware.py

from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponseForbidden


class Redirect403ToLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if isinstance(response, HttpResponseForbidden):
            # Check if the user is not authenticated and redirect to login
            if not request.user.is_authenticated:
                return redirect(settings.LOGIN_URL)
        return response
