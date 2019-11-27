from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    text = 'I LIKE FOOD IS POTATOE.'
    return render(request, 'index.html', {'text': text})

# class IndexView(generic.ListView):
#     template_name = 'staple/index.html'

@login_required
def new_packet(request):
    return render(request, 'new_packet.html')