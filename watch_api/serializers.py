from rest_framework import serializers
from .models import watch_movie,watch_platform

class MovieModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    movie_name = serializers.CharField(max_length=20);
    platform_name = serializers.CharField(max_length = 50, default=None)
    director_name = serializers.CharField(max_length=30);
    story_line = serializers.CharField(max_length=120, default="NA");
    release_year = serializers.IntegerField();
    rating = serializers.FloatField();
    
    def create(self, validated_data):
        """
        Create and return a new `watch_movie` instance, given the validated data.
        """
        return watch_movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `watch_movie` instance, given the validated data.
        """
        instance.movie_name = validated_data.get('movie_name', instance.movie_name)
        instance.director_name = validated_data.get('director_name', instance.director_name)
        instance.story_line = validated_data.get('story_line', instance.story_line)
        instance.release_year = validated_data.get('release_year', instance.release_year)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance

class PlatformModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Platform = serializers.CharField(max_length=20),
    platform_name = serializers.CharField(max_length = 50, default=None)
    Platform_url = serializers.URLField()


    def create(self, validated_data):
        """
        Create and return a new `watch_platform` instance, given the validated data.
        """
        return watch_platform.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `watch_platform` instance, given the validated data.
        """
        instance.Platform = validated_data.get('Platform', instance.Platform)
        instance.platform_name = validated_data.get('platform_name', instance.platform_name)
        instance.Platform_url = validated_data.get('Platform_url', instance.Platform_url)
        instance.save()
        return instance
