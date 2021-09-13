from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    re_path(
        r'^api$',
        views.ApiView.as_view(),
        name='api_view'
    )
]
