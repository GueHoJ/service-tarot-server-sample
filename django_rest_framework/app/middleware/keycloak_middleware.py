# middleware/keycloak_middleware.py

import requests
from django.conf import settings
from django.http import JsonResponse


class KeycloakMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            keycloak_url = f"{settings.KEYCLOAK_SERVER_URL}/auth/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/userinfo"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(keycloak_url, headers=headers)
            if response.status_code != 200:
                return JsonResponse({'detail': 'Invalid token'}, status=401)

        return self.get_response(request)
