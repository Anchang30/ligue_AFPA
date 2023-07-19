# A propos du projet django 'tournament':

Dans le cadre de notre POEI au sein de l'AFPA, nous avons à présenter un projet pour valider la certification CDA (Concepteur Développeur d'Applications). Travaillant déjà au sein de l'entreprise EVIDEN (ex-ATOS), certains de nos projets clients que nous allons présenter en dossier technique couvrent une partie des critères d'évaluation, mais pas tous. Dans le but de valider toutes les compétences du RNCP CDA, nous avons décidé de réaliser un projet personnel afin de valider les critères restants.

Nous avons décidé, Vincent Lavilley et Marvin Marie-Louise, de réaliser un projet de ligue de football en Python dans le framework Django.

Celui-ci comprendra un site web (et une application mobile ??) qui propose de consulter:

    - les résultats d'un match précis avec détails de la rencontre (à définir)
    - un classement dynamique des équipes avec  (POSITION CLUB POINTS JOUÉS GAGNÉS NULS PERDUS BUTS POUR BUTS CONTRE DIFF.)
    - un classement des meilleurs buteurs

Nous pensons également implémenter : 
    - un calendrier des prochains matchs (??)


Le site web s'inspire de https://www.ligue1.fr/ et sera structuré autour  :

    - d'un accueil (index) possèdant des liens pointants vers les autres rubriques
    - d'une liste des résultats des matchs de la dernière journée (possibilité d'ajouter les journées précédentes)
    - d'un classement de la ligue (possibilité d'ajouter les classements des journées précédentes)
    - d'un classement des meilleurs buteurs (possibilité d'ajouter d'autres classements par statistique et les classements antérieurs)

Afin de récupérer et rajouter les nouvelles données à notre BDD, nous aimerions nous connecter à l'API https://www.api-football.com/documentation-v3#section/Introduction

Accès :
VinMar
mon_adresse_eviden
wvZ2X!96L!di7Da<9aP

API_key : 75a37ef9a9msh7007ea31089e9a2p1b8d8bjsn6f08f8c5b5ed

Exemples de requêtes avec le package requests de Python (à choisir) : https://rapidapi.com/api-sports/api/api-football/