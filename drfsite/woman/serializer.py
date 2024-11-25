from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomanSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=False)
    cat_id = serializers.IntegerField()



#
#
# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = WomanSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title": "Angelina Jolie", "content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomanSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
