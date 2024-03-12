from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
# Create your views here.
def watch_list(request):

    movie_list = watch_movie.objects.all()
    serializers_movie=MovieModelSerializer(movie_list, many=True)
    return JsonResponse(serializers_movie.data, safe=False)

def watch_list_by_id(request,pk):

    movie_list_by_id = watch_movie.objects.get(pk = pk)
    serializer_movie_by_id =MovieModelSerializer(movie_list_by_id)

    return JsonResponse(serializer_movie_by_id.data)

def platform_list(request):

    platform_list_movie = watch_platform.objects.all()
    serializers_platform = PlatformModelSerializer(platform_list_movie,many=True)
    return JsonResponse(serializers_platform.data,safe=False)

def platform_list_by_id(request,pk):

    platform_list_by_id = watch_platform.objects.get(pk=pk)
    serializers_platform_by_id = PlatformModelSerializer(platform_list_by_id)
    return JsonResponse(serializers_platform_by_id.data)