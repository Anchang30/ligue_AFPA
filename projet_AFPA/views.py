from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return HttpResponse("Coucou tout le monde, voici mon site web qui présente des \
                        résultats divers et variés sur la ligue 1")
    
def classement(request):
    template = loader.get_template("classement.html")
    return HttpResponse(template.render())