from django.urls import path
from django.views.generic.base import RedirectView
from .adapter._in.custom_login_view_controller import CustomLoginView
from django.contrib.auth import views as auth_views

app_name = 'redirect'
urlpatterns = [
    # Root redirect
    path('', RedirectView.as_view(url='login/', permanent=False), name='root_redirect'),
    # Custom login view
    path('login/', CustomLoginView.as_view(), name='login'),
]
