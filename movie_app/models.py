from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name="Директор")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100 , blank=False, verbose_name="Навзание")
    description = models.TextField(max_length=1000, verbose_name="Описание")
    duration = models.PositiveIntegerField(blank=False, verbose_name="Продолжительность")
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=1000, verbose_name="Коментарий", blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Коментарий {self.text} к фильму {self.movie}"


