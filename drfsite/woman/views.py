from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializer import WomanSerializer


# Create your views here.

class WomanAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomanSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],

        )

        return Response({'post': WomanSerializer(post_new).data})

# class WomanAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomanSerializer
