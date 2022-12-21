from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home, name='home'),
    path('search/', search, name='search'), 
    path('moviepage', moviepage, name='moviepage'), 
    path('upcomingpage', upcomingpage, name='upcomingpage'),
    path("view_trendings_results/<int:id>/", view_trendings_results, name="view_trendings_results"),
    path("populermovie/<int:id>/", populermovie, name="populermovie"),
    path("upcoming/<int:id>/", upcoming, name="upcoming"),
    path("toprated/<int:id>/", toprated, name="toprated"),
    path('tvpopular/<int:id>/', tvpopular, name='tvpopular'),
    path('tvairingtoday/<int:id>/', tvairingtoday, name='tvairingtoday'),
    path('tvtoprated/<int:id>/', tvtoprated, name='tvtoprated'),
    # path("view_search_results/<int:id>/", view_search_results, name="view_search_results"),
    path('detailsearch/<int:id>/', detailsearch, name='detailsearch'),
    path('dashboard/', include('dashboard.urls')),

    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout_view, name='logout'),

    path('blog', blog, name='blog'),

    path('addbookmarktrending/<int:id>/', addbookmarktrending, name='addbookmarktrending'),

    path('aboutme', aboutme, name='aboutme'),

]
