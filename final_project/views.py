from bs4 import BeautifulSoup
from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from final_project.models import *
from .models import Match

import requests

a_matches = []
b_matches = []

#create a request object to get the url
a_today = requests.get("https://www.cbf.com.br/futebol-brasileiro/jogosdehoje/campeonato-brasileiro-serie-a")
b_today = requests.get("https://www.cbf.com.br/futebol-brasileiro/jogosdehoje/campeonato-brasileiro-serie-b")
#create a BeautifulSoup object based on request object
soup_a_today = BeautifulSoup(a_today.content, 'html.parser')
soup_b_today = BeautifulSoup(b_today.content, 'html.parser')

a_matches_today = soup_a_today.findAll("div", {"class": ["block"]})
b_matches_today = soup_b_today.findAll("div", {"class": ["block"]})

Match.objects.all().delete()

for a_match in a_matches_today:
    a_match = Match.objects.create(
        local=a_match.find(class_='text-2 pull-right p-t-15 p-r-10 hidden-lg hidden-md').get_text(),
        local_img = a_match.find(class_='icon escudo x54 pull-right')['src'],
        
        visitor=a_match.find(class_='text-2 pull-left p-t-15 p-l-10 hidden-lg hidden-md').get_text(),
        visitor_img = a_match.find(class_='icon escudo x54 pull-left')['src'],
        
        date=a_match.find(class_='text-1 m-b-10 text-center uppercase').get_text(),
        place=a_match.find(class_='text-1 m-t-10 text-center uppercase').get_text()
    )
    a_matches.append(a_match)

for b_match in b_matches_today:
    b_match = Match.objects.create(
        local=b_match.find(class_='text-2 pull-right p-t-15 p-r-10 hidden-lg hidden-md').get_text(),
        local_img = b_match.find(class_='icon escudo x54 pull-right')['src'],
        
        visitor=b_match.find(class_='text-2 pull-left p-t-15 p-l-10 hidden-lg hidden-md').get_text(),
        visitor_img = b_match.find(class_='icon escudo x54 pull-left')['src'],
        
        date=b_match.find(class_='text-1 m-b-10 text-center uppercase').get_text(),
        place=b_match.find(class_='text-1 m-t-10 text-center uppercase').get_text()
    )
    b_matches.append(b_match)
    
def home(request):
    
    context = {
        'a_matches':a_matches,
        'b_matches': b_matches,
        'matches': Match.objects.all().order_by("date")
    }
    return render(request, 'final_project/home.html', context)

def about(request):
    return render(request, 'final_project/about.html')
