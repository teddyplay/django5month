from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Director, Movie, Review
from movie_app.serializer import *


@api_view(['GET'])
def director_view(request, pk=None):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_director(request, id):
    director = get_object_or_404(Director, id=id)
    serializer = DirectorSerializer(director)
    return Response(serializer.data)



@api_view(['GET'])
def list_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_movies(request, id):
    movies = get_object_or_404(Movie, id=id)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)


@api_view(["GET"])
def list_review(request):
    review = Review.objects.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_review(request, id):
    reviews = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(reviews)
    return Response(serializer.data)




