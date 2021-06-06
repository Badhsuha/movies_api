from .models import Movies
from rest_framework import serializers



class MovieSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = (
            'id', 'title', 'genres', 'createdAt', 'updateAt'
        )

