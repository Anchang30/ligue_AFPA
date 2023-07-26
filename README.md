# A propos du projet django "Ligue_AFPA":

Dans le cadre de la POEI au sein de l'AFPA, je dois présenter un projet pour valider la certification CDA (Concepteur Développeur d'Applications). Travaillant déjà au sein de l'entreprise EVIDEN (BULL, ATOS), j'ai décidé de présenter en dossier technique un projet client couvrant une partie des critères d'évaluation, mais pas tous. Dans le but de valider toutes les compétences du RNCP CDA, j'ai décidé de réaliser un projet personnel afin de valider les critères restants.

                                    -------------------------------------------------------------------------------------------

J'ai de réaliser un projet de ligue de football en Python dans le framework Django. Celui-ci comprendra un site web qui propose de consulter:

    - les résultats des rencontres pour une journée (un week-end dispatché en 3 jours : VE, SA, DI)
    - un classement des équipes selon les journées
    - un classement des meilleurs buteurs

J'aimerais également implémenter : 
    - un calendrier des prochains matchs
    - l'accessibilité du site sur mobile, pour valider un critère supplémentaire
    - des statistiques joueurs supplémentaires: meilleur passeur, meilleur gardien, etc ...

Le site web s'inspire de https://www.ligue1.fr/ et sera structuré autour  :

    - d'un accueil (index) possèdant des liens pointants vers les autres rubriques
    - d'une liste des résultats des matchs de la dernière journée (possibilité d'ajouter les journées précédentes)
    - d'un classement de la ligue (possibilité d'ajouter les classements des journées précédentes)
    - d'un classement des meilleurs buteurs (possibilité d'ajouter d'autres classements par statistique et les classements antérieurs)

                                    -------------------------------------------------------------------------------------------
                                    
** La première implémentation pour servir de POC sera de proposer un classement en fonction des journées disputées (par exemple, pour la seconde journée, je peux
consulter le classement de cette journée, même si le championnat en est à sa 25ème journée). 
Ce classement affichera : 
le placement dans le classement (1,2,3) ; le logo de l'équipe ; le nb de points ; le nombre de match joués : gagnés, perdus, nuls ;  
le nombre de buts mis, encaissés et la différence de buts.

Cela me permettra de me faire la main avec Django et la manipulation des objets.

                                    -------------------------------------------------------------------------------------------

** Ensuite, j'implémenterai une liste des rencontres en fonction des journées : 
date de la journée (vendredi, samedi, dimanche) ; logo de l'équipe domicile ; le score ; le logo de l'équipe visiteur

                                    -------------------------------------------------------------------------------------------
** En dernier lieu, je souhaite intégrer un classement des meilleurs buteurs. Comme les étapes précédentes, il sera possible de visualiser les données pour n'importe quelle journée 
disputée que l'utilisateur choisira.
Ce classement affichera :
la position du joueur dans le classement, ses prénoms/nom, son club avec le logo, le nb de buts à cette journée.
Il sera possible d'ajouter des éléments supplémentaires, car disponibles dans la requête API (pénaltys, passes, nb de match, temps joué, etc ...)

                                    -------------------------------------------------------------------------------------------


Afin de récupérer et rajouter les nouvelles données à notre BDD,  je me connecterai à l'API https://www.api-football.com/documentation-v3#section/Introduction

Accès :
VinMar
mon_adresse_eviden
wvZ2X!96L!di7Da<9aP

API_key : 75a37ef9a9msh7007ea31089e9a2p1b8d8bjsn6f08f8c5b5ed

Exemples de requêtes avec le package requests de Python (à choisir) : https://rapidapi.com/api-sports/api/api-football/