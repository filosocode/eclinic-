from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.pacientes.views import PacienteViewSet
from apps.citas.views import CitaViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)
router.register(r'citas', CitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]