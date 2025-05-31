# Django settings from Vault
SECRET_KEY = "{{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.secret_key }}{{ end }}"

POSTGRES_ENGINE = "{{ with secret "secret/db-creds/postgres/local/properties" }}{{ .Data.data.engine }}{{ end }}"
POSTGRES_DB = "{{ with secret "secret/db-creds/postgres/local/properties" }}{{ .Data.data.db_name }}{{ end }}"
POSTGRES_DB_TAROT = "{{ with secret "secret/db-creds/postgres/local/properties" }}{{ .Data.data.db_name_tarot }}{{ end }}"
POSTGRES_USER = "{{ with secret "secret/db-creds/postgres/local/properties" }}{{ .Data.data.username }}{{ end }}"
POSTGRES_PASSWORD = "{{ with secret "secret/db-creds/postgres/local/properties" }}{{ .Data.data.password }}{{ end }}"
POSTGRES_HOST = "{{ with secret "secret/db-creds/postgres/local/properties" }}{{ .Data.data.host }}{{ end }}"
POSTGRES_PORT = "{{ with secret "secret/db-creds/postgres/local/properties" }}{{ .Data.data.port }}{{ end }}"

DATABASES = {
    'default': {
        'ENGINE': POSTGRES_ENGINE,
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}
# Basic test template
TEST_VARIABLE = "Vault Agent is working"
# test dynamic fetch from ui
TEST_UI_DYNAMIC = "{{ with secret "secret/test/testpath/testvar" }}{{ .Data.data.var }}{{ end }}"

ALLOWED_HOSTS = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.allowed_host }}{{ end }}

CORS_ALLOW_ALL_ORIGINS = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.cors_allow_all_origins }}{{ end }}
CORS_ALLOW_METHODS = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.cors_allow_methods }}{{ end }}
CORS_ALLOW_CREDENTIALS = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.cors_allow_credentials }}{{ end }}

CORS_ALLOWED_HEADERS = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.cors_allowed_headers }}{{ end }}
CORS_ALLOWED_ORIGINS = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.cors_allowed_origins }}{{ end }}
CSRF_TRUSTED_ORIGINS = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.csrf_trusted_origins }}{{ end }}
# Set CSRF_COOKIE_SECURE on production
CSRF_COOKIE_SECURE = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.csrf_cookie_secure }}{{ end }}

DJANGO_SUPERUSER_USERNAME = "{{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.django_superuser_username }}{{ end }}"
DJANGO_SUPERUSER_PASSWORD = "{{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.django_superuser_password }}{{ end }}"
DJANGO_SUPERUSER_EMAIL = "{{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.django_superuser_email }}{{ end }}"

DEBUG = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.debug }}{{ end }}

KEYCLOAK_SERVER_URL = "{{ with secret "secret/django-rest-framework/local/keycloak" }}{{ .Data.data.keycloak_server_url }}{{ end }}"
KEYCLOAK_REALM = "{{ with secret "secret/django-rest-framework/local/keycloak" }}{{ .Data.data.keycloak_realm }}{{ end }}"
KEYCLOAK_CLIENT_ID = "{{ with secret "secret/django-rest-framework/local/keycloak" }}{{ .Data.data.keycloak_client_id }}{{ end }}"
KEYCLOAK_CLIENT_SECRET = "{{ with secret "secret/django-rest-framework/local/keycloak" }}{{ .Data.data.keycloak_client_secret }}{{ end }}"
KEYCLOAK_ADMIN_USERNAME = "{{ with secret "secret/django-rest-framework/local/keycloak" }}{{ .Data.data.keycloak_admin_username }}{{ end }}"
KEYCLOAK_ADMIN_PASSWORD = "{{ with secret "secret/django-rest-framework/local/keycloak" }}{{ .Data.data.keycloak_admin_password }}{{ end }}"
KEYCLOAK_PUBLIC_KEY = (
    "-----BEGIN PUBLIC KEY-----\n"
    "{{ with secret "secret/django-rest-framework/local/keycloak" }}{{ .Data.data.keycloak_public_key }}{{ end }}\n"
    "-----END PUBLIC KEY-----"
)

OLLAMA_URL = {{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.ollama_url }}{{ end }}

OPENAI_API_KEY = "{{ with secret "secret/django-rest-framework/local/settings" }}{{ .Data.data.openai_api_key }}{{ end }}"