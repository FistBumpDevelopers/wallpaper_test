from django.shortcuts import render
from .models import Wallpaper
from taggit.models import Tag
from django.shortcuts import render
from django.db.models import Q
import gensim
import psycopg2
from django.shortcuts import render
# Create your views here.


def index(request):
    all_tags = Tag.objects.all()
    tag_count = {}
    for tag in all_tags:
        tag_count[tag.name] = tag.taggit_taggeditem_items.count()
    tags = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)[:20]
    tags = [ tuple[0] for tuple in tags ]
    trend = Wallpaper.objects.all().filter(Dimentions='Desktop').order_by('-created_at')[:12]
    trend_list = list(trend)
    print(trend_list)
    return render(request,'index.html',{ 'tags':tags,'trend':trend_list})

def wallpaper(request,sauce):
    tags = Tag.objects.all()
    tags = sorted(tags)
    games = Wallpaper.objects.all().filter(my_choice_field='GM').values_list('Sauce', flat=True).distinct()

    distinct_games = []
    for item in games:
        if item not in distinct_games:
            distinct_games.append(item)
    print(distinct_games)

    animes = Wallpaper.objects.all().filter(my_choice_field='AN').values_list('Sauce', flat=True).distinct()
    
    distinct_animes = []
    for item in animes:
        if item not in distinct_animes:
            distinct_animes.append(item)
    print(distinct_animes)

    
    # do something with the filtered wallpapers

    if sauce=='all':
        titles = Wallpaper.objects.all().order_by('-created_at')
    else:
        titles = Wallpaper.objects.all()
        if titles:
            if sauce in [obj.Sauce for obj in titles]:
                # filter by tag
                titles = titles.filter(Sauce=sauce)
                
            else:
                # filter by title
                titles = titles.filter(tags__name=sauce)

    # filtering 
    count=[]
    categories = request.GET.getlist('check-box')
    if categories:
        count.append(1)

    print(count)
    wallpapers = titles.filter(Dimentions__in=categories)
    
    return render(request,'wallpaper.html',{ 'tags':tags, 'games':distinct_games,'animes':distinct_animes,'titles':titles,'wallpapers':wallpapers,'count':count,'sauce':sauce})


# from django.db.models import Q

# def filter(request):
    
#     categories = request.GET.getlist('check-box')
#     print(categories)
#     wallpapers = Wallpaper.objects.filter(Dimentions__in=categories)
#     # do something with the filtered wallpapers
#     return render(request,'filter.html',{'wallpapers':wallpapers})

def results(request):
    tags = Tag.objects.all()
    tags = sorted(tags)
    games = Wallpaper.objects.all().filter(my_choice_field='GM').values_list('Sauce', flat=True).distinct()

    distinct_games = []
    for item in games:
        if item not in distinct_games:
            distinct_games.append(item)

    animes = Wallpaper.objects.all().filter(my_choice_field='AN').values_list('Sauce', flat=True).distinct()
    
    distinct_animes = []
    for item in animes:
        if item not in distinct_animes:
            distinct_animes.append(item)


    search_term = request.GET.get('searchterm', '')

    titles = []

    titles = Wallpaper.objects.all()
      

    # filtering 
    count=[]
    categories = request.GET.getlist('check-box')
    if categories:
        count.append(1)
    wallpapers = titles.filter(Dimentions__in=categories)

    return render(request,'results.html',{ 'tags':tags, 'games':distinct_games,'animes':distinct_animes,'titles':titles,'wallpapers':wallpapers,'count':count,"searchterm":search_term})


def download(request,id):
    tags = Tag.objects.all()
    tags = sorted(tags)
    games = Wallpaper.objects.all().filter(my_choice_field='GM').values_list('Sauce', flat=True).distinct()
    image = Wallpaper.objects.get(id=id)
    distinct_games = []
    for item in games:
        if item not in distinct_games:
            distinct_games.append(item)

    animes = Wallpaper.objects.all().filter(my_choice_field='AN').values_list('Sauce', flat=True).distinct()
    
    distinct_animes = []
    for item in animes:
        if item not in distinct_animes:
            distinct_animes.append(item)

    return render(request,'download.html',{ 'tags':tags, 'games':distinct_games,'animes':distinct_animes,'image':image})