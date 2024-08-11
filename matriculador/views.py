from rest_framework import viewsets

from matriculador.models import Estudante,Curso
from matriculador.serializers import EstudanteSerializer, CursoSerializer

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer