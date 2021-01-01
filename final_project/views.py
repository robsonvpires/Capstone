from django.shortcuts import render
from django.http import HttpResponse

matches = [
    {
        'local': 'Grêmio',
        'visitor': 'Inter',
        'place': 'Arena do Grêmio',
        'date': '16/10/20'
    },
    {
        'local': 'Juventude',
        'visitor': 'Caxias',
        'place': 'Alfredo Jaconi',
        'date': '17/10/20'
    },
]
def home(request):

    context = {
        'matches': matches
    }
    return render(request, 'final_project/home.html', context)

def about(request):
    return render(request, 'final_project/about.html')
