from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'main/index.html')
def hip_hop(request):
    return render(request, 'main/hiphop.html')
def alt_rock(request):
    return render(request, 'main/altrock.html')
def myjam(request):
    return render(request, 'main/myjam.html')
def auto_radio(request):
    return render(request, 'main/autoradio.html')
def club_dance(request):
    return render(request, 'main/clubdance.html')
def deep_house(request):
    return render(request, 'main/deephouse.html')


