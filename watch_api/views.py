from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from django.http import JsonResponse
from rest_framework.reverse import reverse
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'watch_movie': reverse('watch_list', request=request, format=format),
        'watch_platform': reverse('platform_list', request=request, format=format)
    })




@api_view(('GET',))
def watch_list(request):
    movie_list = watch_movie.objects.all()
    serializers_movie = MovieModelSerializer(movie_list, many=True)
    return Response(serializers_movie.data)
@api_view(('GET','PUT','DELETE'))
def watch_list_by_id(request, pk):
    if request.method == 'GET':
        try:
            movie_list_by_id = watch_movie.objects.get(pk=pk)
            serializers_movie_by_id = MovieModelSerializer(movie_list_by_id)
            return Response(serializers_movie_by_id.data)
        except watch_movie.DoesNotExist:
            return Response(serializers_movie_by_id.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        serializers_movie_add = MovieModelSerializer(data=request.data)
        if serializers_movie_add.is_valid():
            serializers_movie_add.save()
            return Response(serializers_movie_add.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_movie_add.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         serializers_movie_add.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(('GET',))
def platform_list(request):
    platform_list = watch_platform.objects.all()
    serializers_platform = PlatformModelSerializer(platform_list,many=True)
    return Response(serializers_platform.data)
@api_view(('GET','PUT','DELETE'))
def platform_list_by_id(request,pk):

    if request.method == 'GET':
        try : 
            platform_list_by_id = watch_platform.objects.get(pk=pk)
            serializers_platform_by_id = PlatformModelSerializer(platform_list_by_id)
            return Response(serializers_platform_by_id.data)
        except Exception as e:
            return Response(serializers_platform_by_id.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        serializers_platform = PlatformModelSerializer(data=request.data)
        if serializers_platform.is_valid():
            serializers_platform.save()
            return Response(serializers_platform.errors, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        serializers_platform.delete() 
        return Response(serializers_platform.errors, status=status.HTTP_200_OK)
        

    
# @api_view(('GET','POST'))
# def watch_list(request):
#     if request.method == 'GET':
#         movie_list = watch_movie.objects.all()
#         serializers_movie=MovieModelSerializer(movie_list, many=True)
#         return Response(serializers_movie.data)
    
#     elif request.method == 'POST':
#         serializer = MovieModelSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(('GET','POST'))
# def watch_list_by_id(request,pk):

#     if request.method == 'GET':
#         movie_list_by_id = watch_movie.objects.get(pk = pk)
#         serializer_movie_by_id =MovieModelSerializer(movie_list_by_id)
#         return Response(serializer_movie_by_id.data)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def watch_list_by_id(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = watch_movie.objects.get(pk=pk)
#     except watch_movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MovieModelSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MovieModelSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     # movie_list_by_id = watch_movie.objects.get(pk = pk)
#     # serializer_movie_by_id =MovieModelSerializer(movie_list_by_id)

#     # return Response(serializer_movie_by_id.data)

# @api_view(('GET','POST'))
# def platform_list(request):
#     if request.method=='GET':
#         platform_list_movie = watch_platform.objects.all()
#         serializers_platform = PlatformModelSerializer(platform_list_movie,many=True)
#         return Response(serializers_platform.data)
    
#     elif request.method == 'POST':
#         serializers_platform = PlatformModelSerializer(data=request.data)
#         if serializers_platform.is_valid():
#             serializers_platform.save()
#             return Response(serializers_platform.data, status=status.HTTP_201_CREATED)
#         return Response(serializers_platform.errors, status=status.HTTP_400_BAD_REQUEST)



# # @api_view(('GET','POST'))
# # def platform_list_by_id(request,pk):

# #     platform_list_by_id = watch_platform.objects.get(pk=pk)
# #     serializers_platform_by_id = PlatformModelSerializer(platform_list_by_id)
# #     return Response(serializers_platform_by_id.data)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def platform_list_by_id(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = watch_platform.objects.get(pk=pk)
#     except watch_platform.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PlatformModelSerializer(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PlatformModelSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)