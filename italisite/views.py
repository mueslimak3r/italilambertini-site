from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('home')
    return render(request, 'homepage.html')

def rings(request):
    return render(request, 'rings.html')

def earrings(request):
    return render(request, 'earrings.html')

def pendants(request):
    return render(request, 'pendants.html')

def customwork(request):
    return render(request, 'custom-work.html')

def ourstory(request):
    return render(request, 'our-story.html')

def contactus(request):
    return render(request, 'contact-us.html')
