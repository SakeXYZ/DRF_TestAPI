from rest_framework import generics
from .models import Women
from .serializer import WomanSerializer


# Create your views here.
class WomanAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomanSerializer
