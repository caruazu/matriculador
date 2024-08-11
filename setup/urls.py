from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from matriculador.views import Estudante, Curso
from matriculador.views import EstudanteViewSet, CursoViewSet

router = routers.DefaultRouter()
router.register('estudante', EstudanteViewSet, basename='Estudante')
router.register('curso', CursoViewSet, basename='Curso')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
