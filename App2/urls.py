from django.contrib import admin
from django.urls import path
from App2.views import display



urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', display),
]