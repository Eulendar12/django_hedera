

from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from core.project.settings import ADMIN_PATH

urlpatterns = [
    path(f'{ADMIN_PATH}/', admin.site.urls),
]
