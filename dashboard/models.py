from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Kategori(models.Model):
    kategori = models.CharField(max_length=100)

    def __str__ (self):
        return self.kategori
    
    class Meta:
        verbose_name_plural = "kategori"


class Artikel(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(
        upload_to='uploads', 
        default='uploads/default.png',
        blank=True, null=True)

    def __str__ (self):
        return "{}. {}".format(self.judul, self.isi,self.cover)
    class Meta:
        verbose_name_plural = "Artikel"


class trendingmovie(models.Model):
    id_trend = models.CharField(max_length=100,blank=True, null=True)
    adult = models.CharField(max_length=100,blank=True, null=True)
    backdrop_path = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    original_language = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField()
    popularity = models.CharField(max_length=100,blank=True, null=True)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    vote_count = models.CharField(max_length=100,blank=True, null=True)


    


class popularmovie(models.Model):
    id_popular = models.CharField(max_length=100,blank=True, null=True)
    adult = models.CharField(max_length=100,blank=True, null=True)
    backdrop_path = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    original_language = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField()
    popularity = models.CharField(max_length=100,blank=True, null=True)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    vote_count = models.CharField(max_length=100,blank=True, null=True)

class upcomingmovie(models.Model):
    id_upcoming = models.CharField(max_length=100,blank=True, null=True)
    adult = models.CharField(max_length=100,blank=True, null=True)
    backdrop_path = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    original_language = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField()
    popularity = models.CharField(max_length=100,blank=True, null=True)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    vote_count = models.CharField(max_length=100,blank=True, null=True)

class topratedmovie(models.Model):
    id_toprated = models.CharField(max_length=100,blank=True, null=True)
    adult = models.CharField(max_length=100,blank=True, null=True)
    backdrop_path = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    original_language = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField()
    popularity = models.CharField(max_length=100,blank=True, null=True)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    vote_count = models.CharField(max_length=100,blank=True, null=True)

class tvpopularmovie(models.Model):
    id_tvpopular = models.CharField(max_length=100,blank=True, null=True)
    adult = models.CharField(max_length=100,blank=True, null=True)
    backdrop_path = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    original_language = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField()
    popularity = models.CharField(max_length=100,blank=True, null=True)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    vote_count = models.CharField(max_length=100,blank=True, null=True)

class tvtopratedmovie(models.Model):
    id_tvtoprated = models.CharField(max_length=100,blank=True, null=True)
    adult = models.CharField(max_length=100,blank=True, null=True)
    backdrop_path = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    original_language = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField()
    popularity = models.CharField(max_length=100,blank=True, null=True)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    vote_count = models.CharField(max_length=100,blank=True, null=True)

class tvairingtodaymovie(models.Model):
    id_tvairingtoday = models.CharField(max_length=100,blank=True, null=True)
    adult = models.CharField(max_length=100,blank=True, null=True)
    backdrop_path = models.CharField(max_length=100,blank=True, null=True)
    name = models.CharField(max_length=100,blank=True, null=True)
    original_language = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField()
    popularity = models.CharField(max_length=100,blank=True, null=True)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    vote_count = models.CharField(max_length=100,blank=True, null=True)
    


   
    
