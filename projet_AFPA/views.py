from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# It will be displayed on the screen, depending on the endpoint it is pointing to.
# Here, http://localhost:8000/ will display the below string in the form of a HttpResponse

def index(request):
    return HttpResponse("Coucou tout le monde, voici mon site web qui présente des \
                        résultats divers et variés sur la ligue 1")
    
def index2(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())