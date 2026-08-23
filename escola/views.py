from django.db.models.functions import Lower
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from escola.models import Estudante, Curso, Matricula
from escola.serializers import (
    EstudanteSerializer,
    CursoSerializer,
    MatriculaSerializer,
    MatriculasPorEstudanteSerializer,
    MatriculasPorCursoSerializer,
)


class ShortPagination(PageNumberPagination):
    page_size = 10


class LongPagination(PageNumberPagination):
    page_size = 20


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.annotate(nome_lower=Lower("nome")).all()
    serializer_class = EstudanteSerializer
    pagination_class = LongPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["nome_lower"]
    ordering = ["nome_lower"]


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    pagination_class = ShortPagination


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculasPorEstudante(generics.ListAPIView):
    def get_queryset(self):  # type: ignore[override]
        queryset = Matricula.objects.filter(estudante_id=self.kwargs["pk"])
        return queryset

    serializer_class = MatriculasPorEstudanteSerializer


class MatriculasPorCurso(generics.ListAPIView):
    def get_queryset(self):  # type: ignore[override]
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset

    serializer_class = MatriculasPorCursoSerializer
