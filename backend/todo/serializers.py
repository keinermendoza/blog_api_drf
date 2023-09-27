from .models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ('id', 'title', 'body',)