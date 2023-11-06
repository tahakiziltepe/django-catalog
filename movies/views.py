from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = "https://api.spoonacular.com/food/menuItems/424571?apiKey=14006651a9d74b35848d659b46964619"
    response = requests.get(url)
    context = response.json()
    info = {}
    info['image'] = context['images'][0]
    info['name'] = context['title']
    list = context['nutrition']['nutrients']
    nutrients = list
    x = 0
    for i in list:
        info[x] = i
        x = x + 1
    return render(request, 'movies/list.html', {"info":info, "nutrients":nutrients})

def detail(request):
    return render(request, 'movies/detail.html')

def search(request):
    return render(request, 'movies/search.html')