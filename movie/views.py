from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login, authenticate, login
from django.contrib.auth import logout
import requests
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.paginator import Paginator

from dashboard.models import *

from .models import *

TMDB_API_KEY = "a1bf5a36c1a72a1e583b4e8d17adcd55"
def search(request):
    global query 
    query = request.GET.get('query')
    URL = "https://api.themoviedb.org/3/search/movie?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae&query={}".format(query)
    
    r = requests.get(url = URL)
    
    data = r.json()
   
    context ={
       
        "data" : data["results"],
        
    }
    return render(request, 'search.html', context)

def detailsearch(request,id):
    URL = "https://api.themoviedb.org/3/search/movie?api_key=9fa77e745db8ea3baef75ce5c9cfc0ae&query={}".format(query)
    r = requests.get(url = URL)
    data = r.json()
    hasil = data['results']
    data = hasil[id]
    contex = {
        'data' : data,
    }
    return render(request, 'detailmovie.html', contex)
    

def home(request):
    data = trendingmovie.objects.all()
    popular = popularmovie.objects.all()
    upcoming = upcomingmovie.objects.all()
    toprated = topratedmovie.objects.all()
    tvpopular = tvpopularmovie.objects.all()
    tvairingtoday = tvairingtodaymovie.objects.all()
    tvtoprated = tvtopratedmovie.objects.all()
    
    return render(request, 'index.html', {
        "data": data,
        "popular": popular,
        "upcoming": upcoming,
        "toprated": toprated,
        "tvpopular": tvpopular,
        "tvairingtoday": tvairingtoday,
        "tvtoprated": tvtoprated,
    })

def moviepage(request):
    template_name = 'front/moviepage/popularpage.html'
    popular = popularmovie.objects.all()

    context = {
        'popular': popular,
    }
    return render(request, template_name, context)

def upcomingpage(request):
    template_name = 'front/moviepage/upcomingpage.html'
    upcoming = upcomingmovie.objects.all()

    context = {
        'upcoming': upcoming,
    }
    return render(request, template_name, context)

    

# def view_tv_detail(request, id):
#     tv = requests.get(f"https://api.themoviedb.org/3/tv/?api_key={TMDB_API_KEY}")
#     data = tv.json()
#     for i in data['results']:
#         if i['id'] == id:
#             return render(request, 'detailmovie.html', {
#                 "data": i,
#                 "type": "tv",
#             })
#         else:
#             continue


def populermovie(request, id):
    popular = popularmovie.objects.all()
    for i in popular:
        if i.id == id:
            return render(request, 'detailmovie.html', {
                "data": i,
                "type": "movie",
            })
        else:
            continue

def upcoming(request,id):
    upcoming = upcomingmovie.objects.all()
    for i in upcoming:
        if i.id == id:
            return render(request, 'detailmovie.html', {
                "data": i,
                "type": "movie",
            })
        else:
            continue

def toprated(request,id):
    toprated = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}")
    data = toprated.json()
    for i in data['results']:
        if i['id'] == id:
            return render(request, 'detailmovie.html', {
                "data": i,
                "type": "movie",
            })
        else:
            continue

def tvpopular(request,id):
    tvpopular = tvpopularmovie.objects.all()
    for i in tvpopular:
        if i.id == id:
            return render(request, 'detailmovie.html', {
                "data": i,
                "type": "tv",
            })
        else:
            continue

def tvairingtoday(request,id):
    tvairingtoday = tvairingtodaymovie.objects.all()
    for i in tvairingtoday:
        if i.id == id:
            return render(request, 'detailmovie.html', {
                "data": i,
                "type": "tv",
            })
        else:
            continue

def tvtoprated(request,id):
    tvtoprated = tvtopratedmovie.objects.all()
    for i in tvtoprated:
        if i.id == id:
            return render(request, 'detailmovie.html', {
                "data": i,
                "type": "tv",
            })
        else:
            continue

def view_trendings_results(request,id):
    data = trendingmovie.objects.all()
    for i in data:
        if i.id == id:
            return render(request, 'detailmovie.html', {
                "data": i,
                "type": "movie",
            })
        else:
            continue

def addbookmarktrending(requests,id):
    data = trendingmovie.objects.all()

    bookmark = trendingmovie.objects.filter(id=id)
    if bookmark.exists():
        messages.error(requests, "Movie already bookmarked")
        return redirect('home')
    else:
        for i in data: 
            if i.id == id:
                trendingmovie.objects.create(
                    id = i.id,
                    title = i.title,
                    overview = i.overview,
                    poster_path = i.poster_path,
                    backdrop_path = i.backdrop_path,
                    release_date = i.release_date,
                    vote_average = i.vote_average,
                    vote_count = i.vote_count,
                    popularity = i.popularity,
                )
                messages.success(requests, "Movie added to bookmark")
                return redirect('home')
            else:
                continue
        
    return redirect('home')
        

        

    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "You have been logged in successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('home')
    else:
        return render(request)

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        make_password(request.POST.get('password'))
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('home')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('home')
        else:
            user = User.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            username=username,
            password=make_password(request.POST.get('password'))
            )
            user.save()
            messages.success(request, "User created successfully")
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'title': 'Register',
        'form': form,

    }
    return render(request,context)

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('home')

def blog(request):
    template = 'blog.html'
    # pagination
    artikel = Artikel.objects.all()
    paginator = Paginator(artikel, 3)
    page = request.GET.get('page')
    venus = paginator.get_page(page)
    context = {
        'venus': venus,
    }
    return render(request, template, context)

def aboutme(request):
    template = 'aboutme.html'
    return render(request, template)