from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse

import requests


def get_html_content(club):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "pt-BR,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    club = club.replace('','+')
    html_content = session.get('https://www.google.com/search?q={club}').text
    return html_content

def home(request): 
    if 'club' in request.GET:
        club = request.GET.get('club')
        html_content = get_html_content(club)
        soup = BeautifulSoup(html_content, 'html.parser')
        match = soup.findAll("div", {"class":"imso_mh__tm-scr imso_mh__mh-bd imso-hov"})
        print('match', match)
        pass

    return render(request, 'finalproject/home.html')

def about(request):
    return render(request, 'finalproject/about.html')

def register(request):
    return render(request, 'finalproject/register.html')
