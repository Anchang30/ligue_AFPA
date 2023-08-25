from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Rencontre, Ligue, Club, Joueur
from .ranking import get_ranking_template, get_score
from .get_data import mapping


def home(request):
    template = loader.get_template("home.html")
    context = {}
    return HttpResponse (template.render(context,request))

# Affiche le classement pour la dernière journée. En choisissant une journée, on peut voir le classement pour celle-ci.
def classement(request, date_journee = 0):
    # filtre par journée
    if not date_journee :
        date_journee = Rencontre.objects.all().last().num_journee  
    # récupère la liste de toutes les rencontre jusqu'à cette date
    rencontre_list = Rencontre.objects.filter(num_journee__lte = date_journee).values()
    # Initialise un classement avec les clubs et des champs = 0
    classement = get_ranking_template()
    # liste des clubs
    liste_clubs = [club.nom for club in Club.objects.all()]
    for club in liste_clubs:
    # récupère les rencontres où le club a joué, à domicile ou à l'extérieur
        rencontre_club = rencontre_list.filter(equipe_dom = mapping.get(club)) | rencontre_list.filter(equipe_vis = mapping.get(club))
        for rencontre in rencontre_club :
    # pour chacun des match de ce club, on calcule le score et MAJ le classement
            get_score(club, classement, rencontre)
            classement[club]["joué"] +=1
            classement[club]["diff"] = classement[club]['buts_mis'] - classement[club]['buts_pris']
    # Trie la liste des clubs pour fournir le classement déjà ordonné
    sorted_ranking = [(rank_+1, club, stats) for rank_, (club,stats)  in enumerate(sorted(classement.items(), key=lambda x:(x[1]["nb_pts"], x[1]["diff"]),reverse = True))]
    # pour obtenir la liste des journées disponibles pour cette saison, pour l'affichage
    liste_nb_journees = [journee for journee in range(1,(((Club.objects.count())-1)*2)+1)]
    template = loader.get_template("classement.html")
    context = {"classement" : sorted_ranking,
               "date_journee":date_journee,
               "rencontres" : rencontre_list,
               "liste_clubs":liste_clubs,
               "journees_liste": liste_nb_journees}
    return HttpResponse(template.render(context, request))


# Affiche la liste des matches pour une journée donnée. Si aucune n'est renseignée, alors la page par défaut
# affiche la dernière journée jouée.
def rencontre(request, date_journee = 0):
    #### AJOuTER UNE VALIDATION QUE LE NOMBRE RENTRE EST BIEN INCLUS DANS LE NB DE JOURNEE MAX :
    #### EX : PAS DE JOURNEE 39 OU 85
    if not date_journee :
        date_journee = Rencontre.objects.all().last().num_journee   
    journee_list = sorted([rencontre for rencontre in Rencontre.objects.all().filter(num_journee = date_journee)], key = lambda r: r.date_match)     
    logos = [(Club.objects.filter(nom=journee.equipe_dom).values("logo")[0]["logo"],Club.objects.filter(nom=journee.equipe_vis).values("logo")[0]["logo"]) for journee in journee_list]
    journee_list_logo = zip(journee_list,logos)
    # pour obtenir la liste des journées disponibles pour cette saison, pour l'affichage
    liste_nb_journees = [journee for journee in range(1,(((Club.objects.count())-1)*2)+1)]
    template = loader.get_template("rencontre.html")
    context = {"journee_list" : journee_list_logo,
               "date_journee": date_journee,
               "journees_liste": liste_nb_journees}
    return HttpResponse(template.render(context, request))
