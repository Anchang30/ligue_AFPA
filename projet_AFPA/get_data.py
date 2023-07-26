import requests
import json
import os

base_url = "https://api-football-v1.p.rapidapi.com/v3/"
headers = {
	"X-RapidAPI-Key": "75a37ef9a9msh7007ea31089e9a2p1b8d8bjsn6f08f8c5b5ed",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
# Chemin d'accès aux données en format json
dir_path = os.path.dirname(os.path.realpath(__file__))
json_path = os.path.dirname(dir_path) + "/data/"
    

def get_ligue1_journees():
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

def clean_ligue1():
    with open(json_path + 'raw/journees_ligue1_2022.json') as f:
        journee_22 = json.load(f)
    journee_clean  = [{"date_match": journee["fixture"]["date"],
                "num_journee" : journee["league"]["round"][-2:].strip(), 
                "equipe_dom":journee["teams"]['home']['name'],
                "equipe_vis": journee["teams"]['away']['name'],
                "buts_dom": journee["goals"]["home"],
                "buts_vis": journee["goals"]["away"]} for journee in journee_22["response"]]
    l1_22_clean = open(json_path + "clean/journees_ligue1_2022_clean.json", "w")
    json.dump(journee_clean, l1_22_clean, indent= 6)
    l1_22_clean.close()
    f.close()
   
if __name__ == '__main__' :
    get_ligue1_journees()
    clean_ligue1()
