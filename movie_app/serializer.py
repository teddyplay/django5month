from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    class Meta:
        model = Director
        fields = ["id", "name" ,"movie_count"]



class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=1000)
    class Meta:
        model = Movie
        fields = ["id", "title", "description",
                  "duration", "director_id", "rating",]

class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=1000)

    class Meta:
        model = Review
        fields = ["id", "text", "stars"]


