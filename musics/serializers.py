from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.Serializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)