from rest_framework import serializers
from .models import Women


class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id', 'content')
