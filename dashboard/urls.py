from django.urls import path,include
from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    # include movie urls
    path('index', index, name='index'),
    path('berita', berita, name='berita'),
    path('berita/lihat/<str:id>',lihat_artikel, name = 'lihat_artikel'),
    path('berita/edit/<str:id>', edit_artikel, name = 'edit_artikel'),
    path('berita/delete/<str:id>', delete_artikel, name = 'delete_artikel'),
    path('beritaartikel', beritaartikel, name='beritaartikel'),
    path('user', user, name='user'),
    path('deleteuser/<str:id>', deleteuser, name='deleteuser'),
    path('trending', trending_sinkron, name='trending'),
    path('popular', popularmovie_sinkron, name='popular'),
    path('upcoming', upcomingmovie_sinkron, name='upcoming'),
    path('toprated', topratedmovie_sinkron, name='toprated'),
    path('tvpopular', tvpopular_sinkron, name='tvpopular'),
    path('tvtoprated', tvtoprated_sinkron, name='tvtoprated'),
    path('tvairingtoday', tvairingtodaymovie_sinkron, name='tvairingtoday'),
    path('edituser/<str:id>', edituser, name='edituser'),

    # path('group/<str:id>',group, name='group')

]

