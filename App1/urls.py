from django.contrib import admin
from django.urls import path

from App1.views import displayDataTime
from App1.views import displayLogin
from App1.views import display

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', display),
    path('ahora/', displayDataTime),
    path('login/', displayLogin),
]