from django.contrib import admin
from .models import *

# Register your models here.
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','cover','judul', 'isi', 'kategori', 'date')
    list_filter = ('kategori', 'date')

class KategoriAdmin(admin.ModelAdmin):
    list_display = ('kategori',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis', 'penerbit', 'tahun','isi', 'cover')
    
class trendingAdmin(admin.ModelAdmin):
    list_display = ('id_trend', 'adult', 'backdrop_path', 'name', 'original_language', 'title', 'image', 'overview', 'popularity', 'date', 'rating', 'vote_count')
    list_filter = ('date','rating')

class popularAdmin(admin.ModelAdmin):
    list_display = ('id_popular', 'adult', 'backdrop_path', 'name', 'original_language', 'title', 'image', 'overview', 'popularity', 'date', 'rating', 'vote_count')
    list_filter = ('date','rating')

class upcomingAdmin(admin.ModelAdmin):
    list_display = ('id_upcoming', 'adult', 'backdrop_path', 'name', 'original_language', 'title', 'image', 'overview', 'popularity', 'date', 'rating', 'vote_count')
    list_filter = ('date','rating')

class toprated(admin.ModelAdmin):
    list_display = ('id_toprated', 'adult', 'backdrop_path', 'name', 'original_language', 'title', 'image', 'overview', 'popularity', 'date', 'rating', 'vote_count')
    list_filter = ('date','rating')

class tvpopularAdmin(admin.ModelAdmin):
    list_display = ('id_tvpopular', 'adult', 'backdrop_path', 'name', 'original_language', 'title', 'image', 'overview', 'popularity', 'date', 'rating', 'vote_count')
    list_filter = ('date','rating')

class tvtopratedAdmin(admin.ModelAdmin):
    list_display = ('id_tvtoprated', 'adult', 'backdrop_path', 'name', 'original_language', 'title', 'image', 'overview', 'popularity', 'date', 'rating', 'vote_count')
    list_filter = ('date','rating')

class tvairingtodayAdmin(admin.ModelAdmin):
    list_display = ('id_tvairingtoday', 'adult', 'backdrop_path', 'name', 'original_language', 'title', 'image', 'overview', 'popularity', 'date', 'rating', 'vote_count')
    list_filter = ('date','rating')
    

    

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Artikel, ArtikelAdmin)

admin.site.register(trendingmovie,trendingAdmin)
admin.site.register(popularmovie,popularAdmin)
admin.site.register(upcomingmovie,upcomingAdmin)
admin.site.register(topratedmovie,toprated)
admin.site.register(tvpopularmovie,tvpopularAdmin)
admin.site.register(tvtopratedmovie,tvtopratedAdmin)
admin.site.register(tvairingtodaymovie,tvairingtodayAdmin)





