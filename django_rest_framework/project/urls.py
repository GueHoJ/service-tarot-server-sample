"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView, RedirectView
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg import openapi
from django.http import HttpResponse

from app.sitemaps import StaticViewSitemap
from redirect.adapter._in.custom_login_view_controller import CustomLoginView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    """
    # CLASS : BothHttpAndHttpsSchemaGenerator
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 11:41 AM
    # DESCRIPTION
        - HTTP and HTTPS
        - https://stackoverflow.com/questions/55568431/how-can-i-configure-https-schemes-with-the-drf-yasg-auto-generated-swagger-pag
    """

    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]
        return schema


schema_url_v1_patterns = [
    path('user/', include('user.urls', namespace='user')),
    path('lang/', include('lang.urls', namespace='lang')),
    path('ollamas/', include('ollamas.urls', namespace='ollamas')),
    path('chatbot/', include('chatbot.urls', namespace='chatbot')),
    path('servicelog/', include('servicelog.urls', namespace='servicelog')),
    path('servicetoken/', include('servicetoken.urls', namespace='servicetoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/expiration/', TokenVerifyView.as_view(), name='token_expiration'),
    # path('/', include('redirect.urls', namespace='redirect')),
]

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="ConAi App Backend Server Open API",
        default_version='v1',
        description="# ConAI INC BACKEND SERVER\n"
                    "---\n"
                    "## API AUTHENTICATION & PERMISSION DESCRIPTION\n"
                    "\n"
                    "### 아래 항목을 request 시 각 영역에 반드시 포함 시켜야 SERVER의 AUTHENTICATION, PERMISSION 체크를 통과 할 수 있습니다.\n"
                    "\n"
                    "\n"
                    "\t\t(향후 firebase remote config 에서 관리 필요) => 관리 중\n"
                    "\n"
                    "\n"
                    "<br/>"
                    "<br/>",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jue@conai.ai"),
        license=openapi.License(name="ConAI Inc"),
    ),
    validators=['flex', 'ssv'],
    public=False,
    generator_class=BothHttpAndHttpsSchemaGenerator,  # HTTP and HTTPS
    # permission_classes=(AllowAny,),
    # 인증된 사용자만 접근 가능하도록 권한 설정
    # permission_classes=[IsAuthenticated],
    # simple jwt 토큰 없이 API DOC UI 접근 가능
    permission_classes=[IsAuthenticated, ],
    # 로그인 후 API DOC UI 접근 가능
    authentication_classes=[SessionAuthentication, BasicAuthentication],
    patterns=schema_url_v1_patterns,
    url=getattr(settings, "HOST_URL")

)


def empty_sitemap(request):
    return HttpResponse(content='', content_type='application/xml')


sitemaps = {
    'static': StaticViewSitemap,
}
urlpatterns = [
                  path('admin/', admin.site.urls),
                  # Serve robots.txt
                  path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
                  # Serve favicon.ico
                  path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
                  # Sitemap URL
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
                  # <!-- django-allauth -->
                  # path('accounts/', include('allauth.urls')),
                  # Auto DRF API docs
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0),
                          name='schema-json'),
                  re_path(r'^swagger(/)?$', schema_view_v1.with_ui('swagger', cache_timeout=0),
                          name='schema-swagger-ui'),
                  re_path(r'^redoc/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
                  path('login/', CustomLoginView.as_view(), name='login'),
                  # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                  # user
                  path('user/', include('user.urls')),
                  # redirect
                  path('', include('redirect.urls')),
                  path('lang/', include('lang.urls')),
                  path('ollamas/', include('ollamas.urls')),
                  path('chatbot/', include('chatbot.urls')),
                  path('servicelog/', include('servicelog.urls')),
                  path('servicetoken/', include('servicetoken.urls')),
                  # JWT Token endpoints
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                  path('api/token/expiration/', TokenVerifyView.as_view(), name='token_expiration'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
