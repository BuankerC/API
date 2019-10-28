from rest_framework import serializers
from .models import Music, Artist, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)

class ArtistSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(source="music_set", many=True)
    class Meta:
        model = Artist
        fields = ('id', 'name',)

class ArtistDetailSerializer(serializers.ModelSerializer):
    musics = MusicSerializer(source="music_set", many=True)
    musics_count = serializers.IntegerField(source="music_set.count")
    class Meta:
        model = Artist
        fields = ('id', 'name', 'musics', 'musics_count')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id')