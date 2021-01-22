from bs4 import BeautifulSoup
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from final_project.models import *
from .models import Match

import requests


#create a request object to get the url
r_today = requests.get("https://www.cbf.com.br/futebol-brasileiro/jogosdehoje/campeonato-brasileiro-serie-b")
#create a BeautifulSoup object based on request object
soup_today = BeautifulSoup(r_today.content, 'html.parser')
     
matches_today = soup_today.findAll("div", {"class": ["block"]})

for match in matches_today:
    match = Match.objects.create(
        local=match.find(class_='text-2 pull-right p-t-15 p-r-10 hidden-lg hidden-md').get_text(),
        #local_img = match.find(class_='col-xs-5 p-t-10 nopadding').get_image(),
        visitor=match.find(class_='text-2 pull-left p-t-15 p-l-10 hidden-lg hidden-md').get_text(),
        date="2020-01-01 18:00",
        place=match.find(class_='text-1 m-t-10 text-center uppercase').get_text()
    )
    
def home(request):
    
    context = {
        'matches': Match.objects.all().order_by("date")
    }
    return render(request, 'final_project/home.html', context)

def about(request):
    return render(request, 'final_project/about.html')
