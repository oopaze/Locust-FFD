from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer

    def get_queryset(self):
        return Pessoa.objects.all()