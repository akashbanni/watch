from django.db import models


# Create your models here.
class watch_movie(models.Model):
    movie_name = models.CharField(max_length=20);
    director_name = models.CharField(max_length=30);
    platform_name = models.CharField(max_length = 50, default= "Netflix");
    story_line = models.CharField(max_length=120);
    release_year = models.IntegerField();
    rating = models.FloatField();

    def __str__(self):
        return self.movie_name + " (" + str(self.release_year) + ")";


    

class watch_platform(models.Model):
    Id = models.ForeignKey(watch_movie, on_delete=models.CASCADE),
    Platform = models.CharField(max_length=20),
    platform_name = models.CharField(max_length = 50)
    Platform_url = models.URLField()

    def __str__(self):
        return  self.platform_name;