import requests
import json
import os
from datetime import datetime

base_url = "https://api-football-v1.p.rapidapi.com/v3/"
headers = {
	"X-RapidAPI-Key": "75a37ef9a9msh7007ea31089e9a2p1b8d8bjsn6f08f8c5b5ed",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

conv_clubs = {'Stade Brestois 29':' STADE BRESTOIS 29',
'Clermont Foot':'CLERMONT FOOT 63',
'Paris Saint Germain' : 'PARIS SAINT-GERMAIN',
'Strasbourg': 'RC STRASBOURG ALSACE',
 'Nice': 'OGC NICE',
 'Auxerre': 'AJ AUXERRE',
 'Angers': 'ANGERS SCO',
 'Ajaccio': 'AC AJACCIO',
 'Montpellier': 'MONTPELLIER HERAULT SC',
 'Marseille': 'OLYMPIQUE DE MARSEILLE',
 'Monaco': 'AS MONACO',
 'Lens': 'RC LENS',
 'Nantes': 'FC NANTES',
 'Lyon': 'OLYMPIQUE LYONNAIS',
 'Rennes': 'STADE RENNAIS FC',
 'Toulouse': 'TOULOUSE FC',
 'Clermont Foot': 'CLERMONT FOOT 63',
 'Reims': 'STADE DE REIMS',
 'Estac Troyes': 'ESTAC TROYES',
 'Lorient': 'FC LORIENT',
 'Lille': 'LOSC LILLE'}


# Chemin d'accès aux données en format json
dir_path = os.path.dirname(os.path.realpath(__file__))
json_path = os.path.dirname(dir_path) + "/data/"
    

def get_journees():
    #Récupère les données des journées de la ligue 1 pour l'année 2022 - 2023
    # A modifier pour prendre en argument la ligue, et l'année ??   
 
    url = base_url + "fixtures"
    # La ligue 61 correspond à la ligue 1.
    params = {"league":"61","season":"2022"}
    response = requests.get(url, headers=headers, params= params)
    journees = response.json() 
    "Ouvre le document json qui va stocker les données de l'API"
    res_ligue1 = open(json_path + "raw/journees_ligue1_2022.json","w")
    # Sauve les données de la variable journee dans le document json res_ligue1
    json.dump(journees, res_ligue1, indent = 6)
    res_ligue1.close()

def clean_journees():
    with open(json_path + 'raw/journees_ligue1_2022.json') as f:
        journee_22 = json.load(f)
    journee_clean  = [{"model": "projet_AFPA.rencontre",
                   "pk": pk+1,
                   "fields": {"date_match": datetime.fromtimestamp(journee["fixture"]["timestamp"]).strftime("%Y-%m-%d"),
                   "num_journee" : journee["league"]["round"][-2:].strip(), 
                   "equipe_dom":journee["teams"]['home']['name'],
                   "equipe_vis": journee["teams"]['away']['name'],
                   "buts_dom": journee["goals"]["home"],
                   "buts_vis": journee["goals"]["away"]}} for pk, journee in enumerate(journee_22["response"])]
    for journee in journee_clean :
        journee["fields"]["equipe_dom"] = conv_clubs.get(journee["fields"]["equipe_dom"])
        journee["fields"]["equipe_vis"] = conv_clubs.get(journee["fields"]["equipe_vis"])
    l1_22_clean = open(json_path + "clean/journees_ligue1_2022_clean.json", "w")
    json.dump(journee_clean, l1_22_clean, indent= 6)
    l1_22_clean.close()
    f.close()
    
# Récupère les données pour les clubs de Ligue 1, saison 2022 - 2023, à partir du json
# Les données sont nettoyées en amont, car trop complexe et besoin d'une action manuelle.
def get_clubs():
    with open(json_path + 'clean/clubs_dict.json') as f:   
        return json.load(f)
   
# Récupère les données pour les clubs de Ligue 1, saison 2022 - 2023.
def get_players() :
    pass
    
    
    
if __name__ == '__main__' :
    get_journees()
    clean_journees()
