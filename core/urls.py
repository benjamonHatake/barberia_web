from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Todas las URL de agenda están aquí
    path('', include('agenda.urls')),
]
