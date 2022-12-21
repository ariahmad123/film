from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
import requests
from .models import *
from django.contrib.auth.models import User
from movie.models import *

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

def trending_sinkron(request):
    trending = trendingmovie.objects.all()
    trending.delete()
    template_name = 'back/sinkron/sinkron.html'
    URL = "https://api.themoviedb.org/3/trending/all/day?api_key=a1bf5a36c1a72a1e583b4e8d17adcd55"
    r = requests.get(URL)
    data = r.json()
    for i in data['results']:
        try:
            original = i['original_name']
            date = i['first_air_date']
            name = i['name']
        except:
            original = i['original_title']
            date = i['release_date']
            name = i['title']

        trending_cek = trendingmovie.objects.filter(id_trend=i['id'])
        if trending_cek.exists():
            trend = trending_cek.first()
            trend.id_trend = i['id']
            trend.adult = i['adult']
            trend.backdrop_path = i['backdrop_path']
            trend.name = name
            trend.original_language = i['original_language']
            trend.title = original
            trend.image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path']
            trend.overview = i['overview']
            trend.popularity = i['popularity']
            trend.date = date
            trend.rating = i['vote_average']
            trend.vote_count = i['vote_count']
            
            
        else:
            trendingmovie.objects.create(
                id_trend = i['id'],
                adult = i['adult'],
                backdrop_path = i['backdrop_path'],
                name = name,
                original_language = i['original_language'],
                title = original,
                image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path'],
                overview = i['overview'],
                popularity = i['popularity'],
                date = date,
                rating = i['vote_average'],
                vote_count = i['vote_count'],

            )
    context = {
        'data1' : data['results'],
        'data' : trending,
    }
    return render(request, template_name, context)

def popularmovie_sinkron(request):
    pop = popularmovie.objects.all()
    pop.delete()
    template_name = 'back/sinkron/sinkron.html'
    URL = "https://api.themoviedb.org/3/movie/popular?api_key=a1bf5a36c1a72a1e583b4e8d17adcd55&language=en-US&page=1"
    r = requests.get(URL)
    data = r.json()
    for i in data['results']:
        try:
            original = i['original_name']
            date = i['first_air_date']
            name = i['name']
        except:
            original = i['original_title']
            date = i['release_date']
            name = i['title']

        popularmovie_cek = popularmovie.objects.filter(id_popular=i['id'])
        if popularmovie_cek.exists():
            popular = popularmovie_cek.first()
            popular.id_popular = i['id']
            popular.adult = i['adult']
            popular.backdrop_path = i['backdrop_path']
            popular.name = name
            popular.original_language = i['original_language']
            popular.title = original
            popular.image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path']
            popular.overview = i['overview']
            popular.popularity = i['popularity']
            popular.date = date
            popular.rating = i['vote_average']
            popular.vote_count = i['vote_count']
   
        else:
            popularmovie.objects.create(
                id_popular = i['id'],
                adult = i['adult'],
                backdrop_path = i['backdrop_path'],
                name = name,
                original_language = i['original_language'],
                title = original,
                image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path'],
                overview = i['overview'],
                popularity = i['popularity'],
                date = date,
                rating = i['vote_average'],
                vote_count = i['vote_count'],

            )
    context = {
        'data1' : data['results'],
        'data' : pop,
    }
    return render(request, template_name, context)

def upcomingmovie_sinkron(request):
    upcom = upcomingmovie.objects.all()
    upcom.delete()
    template_name = 'back/sinkron/sinkron.html'
    URL = "https://api.themoviedb.org/3/movie/upcoming?api_key=a1bf5a36c1a72a1e583b4e8d17adcd55&language=en-US&page=1"
    r = requests.get(URL)
    data = r.json()
    for i in data['results']:
        try:
            original = i['original_name']
            date = i['first_air_date']
            name = i['name']
        except:
            original = i['original_title']
            date = i['release_date']
            name = i['title']

        upcomingmovie_cek = upcomingmovie.objects.filter(id_upcoming=i['id'])
        if upcomingmovie_cek.exists():
            upcoming = upcomingmovie_cek.first()
            upcoming.id_upcoming = i['id']
            upcoming.adult = i['adult']
            upcoming.backdrop_path = i['backdrop_path']
            upcoming.name = name
            upcoming.original_language = i['original_language']
            upcoming.title = original
            upcoming.image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path']
            upcoming.overview = i['overview']
            upcoming.popularity = i['popularity']
            upcoming.date = date
            upcoming.rating = i['vote_average']
            upcoming.vote_count = i['vote_count']
            
            
        else:
            upcomingmovie.objects.create(
                id_upcoming = i['id'],
                adult = i['adult'],
                backdrop_path = i['backdrop_path'],
                name = name,
                original_language = i['original_language'],
                title = original,
                image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path'],
                overview = i['overview'],
                popularity = i['popularity'],
                date = date,
                rating = i['vote_average'],
                vote_count = i['vote_count'],

            )
    context = {
        'data1' : data['results'],
        'data' : upcom,
    }
    return render(request, template_name, context)

def topratedmovie_sinkron(request):
    top = topratedmovie.objects.all()
    top.delete()
    template_name = 'back/sinkron/sinkron.html'
    URL = "https://api.themoviedb.org/3/movie/top_rated?api_key=a1bf5a36c1a72a1e583b4e8d17adcd55&language=en-US&page=1"
    r = requests.get(URL)
    data = r.json()
    for i in data['results']:
        try:
            original = i['original_name']
            date = i['first_air_date']
            name = i['name']
        except:
            original = i['original_title']
            date = i['release_date']
            name = i['title']

        topratedmovie_cek = topratedmovie.objects.filter(id_toprated=i['id'])
        if topratedmovie_cek.exists():
            toprated = topratedmovie_cek.first()
            toprated.id_toprated = i['id']
            toprated.adult = i['adult']
            toprated.backdrop_path = i['backdrop_path']
            toprated.name = name
            toprated.original_language = i['original_language']
            toprated.title = original
            toprated.image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path']
            toprated.overview = i['overview']
            toprated.popularity = i['popularity']
            toprated.date = date
            toprated.rating = i['vote_average']
            toprated.vote_count = i['vote_count']
            
            
        else:
            topratedmovie.objects.create(
                id_toprated = i['id'],
                adult = i['adult'],
                backdrop_path = i['backdrop_path'],
                name = name,
                original_language = i['original_language'],
                title = original,
                image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path'],
                overview = i['overview'],
                popularity = i['popularity'],
                date = date,
                rating = i['vote_average'],
                vote_count = i['vote_count'],

            )
    context = {
        'data1' : data['results'],
        'data' : top,
    }
    return render(request, template_name, context)

def tvpopular_sinkron(request):
    tvpop = tvpopularmovie.objects.all()
    tvpop.delete()
    template_name = 'back/sinkron/sinkron.html'
    URL = "https://api.themoviedb.org/3/tv/popular?api_key=a1bf5a36c1a72a1e583b4e8d17adcd55&language=en-US&page=1"
    r = requests.get(URL)
    data = r.json()
    for i in data['results']:
        try:
            original = i['original_name']
            date = i['first_air_date']
            name = i['name']
        except:
            original = i['original_title']
            date = i['release_date']
            name = i['title']

        popular_cek = tvpopularmovie.objects.filter(id_tvpopular=i['id'])
        if popular_cek.exists():
            popular = popular_cek.first()
            popular.id_tvpopular = i['id']
            popular.backdrop_path = i['backdrop_path']
            popular.name = name
            popular.original_language = i['original_language']
            popular.title = original
            popular.image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path']
            popular.overview = i['overview']
            popular.popularity = i['popularity']
            popular.date = date
            popular.rating = i['vote_average']
            popular.vote_count = i['vote_count']
            
            
        else:
            tvpopularmovie.objects.create(
                id_tvpopular = i['id'],
                backdrop_path = i['backdrop_path'],
                name = name,
                original_language = i['original_language'],
                title = original,
                image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path'],
                overview = i['overview'],
                popularity = i['popularity'],
                date = date,
                rating = i['vote_average'],
                vote_count = i['vote_count'],

            )
    context = {
        'data1' : data['results'],
        'data' : tvpop,
    }
    return render(request, template_name, context)

def tvtoprated_sinkron(request):
    tvtop = tvtopratedmovie.objects.all()
    tvtop.delete()
    template_name = 'back/sinkron/sinkron.html'
    URL = "https://api.themoviedb.org/3/tv/top_rated?api_key=a1bf5a36c1a72a1e583b4e8d17adcd55&language=en-US&page=1"
    r = requests.get(URL)
    data = r.json()
    for i in data['results']:
        try:
            original = i['original_name']
            date = i['first_air_date']
            name = i['name']
        except:
            original = i['original_title']
            date = i['release_date']
            name = i['title']

        toprated_cek = tvtopratedmovie.objects.filter(id_tvtoprated=i['id'])
        if toprated_cek.exists():
            toprated = toprated_cek.first()
            toprated.id_tvtoprated = i['id']
            toprated.backdrop_path = i['backdrop_path']
            toprated.name = name
            toprated.original_language = i['original_language']
            toprated.title = original
            toprated.image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path']
            toprated.overview = i['overview']
            toprated.popularity = i['popularity']
            toprated.date = date
            toprated.rating = i['vote_average']
            toprated.vote_count = i['vote_count']
            
            
        else:
            tvtopratedmovie.objects.create(
                id_tvtoprated = i['id'],
                backdrop_path = i['backdrop_path'],
                name = name,
                original_language = i['original_language'],
                title = original,
                image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path'],
                overview = i['overview'],
                popularity = i['popularity'],
                date = date,
                rating = i['vote_average'],
                vote_count = i['vote_count'],

            )
    context = {
        'data1' : data['results'],
        'data' : tvtop,
    }
    return render(request, template_name, context)

def tvairingtodaymovie_sinkron(request):
    tvairing = tvairingtodaymovie.objects.all()
    tvairing.delete()
    template_name = 'back/sinkron/sinkron.html'
    URL = "https://api.themoviedb.org/3/tv/on_the_air?api_key=a1bf5a36c1a72a1e583b4e8d17adcd55&language=en-US&page=1"
    r = requests.get(URL)
    data = r.json()
    for i in data['results']:
        try:
            original = i['original_name']
            date = i['first_air_date']
            name = i['name']
        except:
            original = i['original_title']
            date = i['release_date']
            name = i['title']

        onair_cek = tvairingtodaymovie.objects.filter(id_tvairingtoday=i['id'])
        if onair_cek.exists():
            onair = onair_cek.first()
            onair.id_tvairingtoday = i['id']
            onair.backdrop_path = i['backdrop_path']
            onair.name = name
            onair.original_language = i['original_language']
            onair.title = original
            onair.image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path']
            onair.overview = i['overview']
            onair.popularity = i['popularity']
            onair.date = date
            onair.rating = i['vote_average']
            onair.vote_count = i['vote_count']
            
            
        else:
            tvairingtodaymovie.objects.create(
                id_tvairingtoday = i['id'],
                backdrop_path = i['backdrop_path'],
                name = name,
                original_language = i['original_language'],
                title = original,
                image = "https://image.tmdb.org/t/p/w500%s" %i['poster_path'],
                overview = i['overview'],
                popularity = i['popularity'],
                date = date,
                rating = i['vote_average'],
                vote_count = i['vote_count'],

            )
    context = {
        'data1' : data['results'],
        'data' : tvairing,
    }
    return render(request, template_name, context)

@login_required 
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'
    template_name = "back/dashboard.html"
    user = User.objects.all()
    context = {
        'title': 'Dashboard',
        'artikel': user,
    }
    return render(request, template_name, context)

@login_required 
def index(request):
   
    artikel = Artikel.objects.all()
    user = User.objects.exclude(is_superuser=True)
    admin = User.objects.filter(is_superuser=True)
    


    context = {
        
        'artikel' : artikel,
        'user' : user,
        'admin' : admin,


    }
    template_name = 'back/index.html'
    return render(request, template_name,context)

def berita(request):
    template_name = 'back/artikel/artikel.html'
    artikel = Artikel.objects.all()
    kategori = Kategori.objects.all()
    if request.method == 'POST':
        judul = request.POST.get('judul')
        isi = request.POST.get('isi')
        cover = request.FILES.get('cover')
        kategory = request.POST.get('kategori')
        penulis = request.user
        
        if judul == '' or isi == '':
            messages.error(request, 'data tidak boleh kosong')
        else:
            kat = Kategori.objects.get(kategori=kategory)
            Artikel.objects.create(
                nama = penulis,
                judul=judul,
                isi=isi,
                kategori=kat,
                cover=cover,
            )
            messages.success(request, 'berhasil di tambahkan')
    context = {
        'title': 'Artikel',
        'artikel': artikel,
        'kategori': kategori,
    }
    return render(request, template_name, context)

def lihat_artikel(request, id):
    artikel = Artikel.objects.get(id=id)
    template_name = 'back/artikel/lihatartikel.html'
    context = {
        'title': 'Artikel',
        'artikel': artikel,
    }
    return render(request, template_name, context)


def edit_artikel(request, id):
    template_name = 'back/artikel/editartikel.html'
    artikel = Artikel.objects.get(id=id)
    if request.method == 'POST':
        judul = request.POST.get('judul')
        isi = request.POST.get('isi')
        cover = request.FILES.get('cover')
        penulis = request.user
        if judul == ''or cover == ''  or isi == '':
            messages.error(request, 'data tidak boleh kosong')
        else:
            artikel.nama = penulis
            artikel.judul = judul
            artikel.isi = isi
            artikel.cover = cover
            artikel.save()
            messages.success(request, 'berhasil di update')
        return redirect('berita')
    
    context = {
        'title': 'Artikel',
        'artikel': artikel,
        
    }
    return render(request, template_name, context)


def delete_artikel(request, id):
    artikel = Artikel.objects.get(id=id)
    artikel.delete()
    messages.error(request, 'berhasil di hapus')
    return redirect('berita')


def beritaartikel(request):
    template_name = 'back/artikel/beritaartikel.html'
    artikel = Artikel.objects.all()
    context = {
        'title': 'Artikel',
        'artikel': artikel,
    }
    return render(request, template_name, context)

@login_required 
@user_passes_test(is_operator)
def user(request):
    template_name = 'back/user/tableuser.html'
    user = User.objects.all()
    context = {
        'title': 'User',
        'user': user,
    }
    return render(request, template_name, context)

@login_required 
@user_passes_test(is_operator)
def deleteuser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.error(request, 'berhasil di hapus')
    return redirect('user')

@login_required 
@user_passes_test(is_operator)
def edituser(request, id):
    template_name = 'back/user/edituser.html'
    user = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username == '' or email == '' or password == '':
            messages.error(request, 'data tidak boleh kosong')
        else:
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()
            messages.success(request, 'berhasil di update')
        return redirect('user')
    
    context = {
        'title': 'User',
        'user': user,
        
    }
    return render(request, template_name, context)

# def group(request,id):
#     my_group = Group.objects.get(name='Operator') 
#     my_group.user_set.add(id)
#     messages.error(request, 'berhasil di hapus')
#     return redirect('user')


