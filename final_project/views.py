from django.shortcuts import render
from django.http import HttpResponse
from final_project.models import *

def home(request):

    context = {
        'matches': Match.objects.all()
    }
    return render(request, 'final_project/home.html', context)

def about(request):
    return render(request, 'final_project/about.html')
