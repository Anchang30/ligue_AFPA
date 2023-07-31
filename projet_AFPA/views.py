from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Rencontre, Ligue, Club, Joueur

def home(request):
    return HttpResponse("Coucou tout le monde, voici mon site web qui présente des \
                        résultats divers et variés sur la ligue 1")
    
def classement(request):
    template = loader.get_template("classement.html")
    context = {}
    return HttpResponse(template.render())

def rencontre(request, date_journee):
    journee_list = sorted([rencontre for rencontre in Rencontre.objects.all().filter(num_journee = date_journee)], key = lambda r: r.date_match)
    template = loader.get_template("rencontre.html")
    context = {"journee_list" : journee_list,
               'date_journee': date_journee}
    return HttpResponse(template.render(context, request))
