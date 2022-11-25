from .models import Crud
from rest_framework import viewsets, permissions
from .serializers import CrudSerializer

class CrudViewSet(viewsets.ModelViewSet):
   queryset = Crud.objects.all()
   permission_classes=[permissions.AllowAny]
   serializer_class= CrudSerializer
