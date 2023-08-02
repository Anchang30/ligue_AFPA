from .get_data import mapping
from .models import Rencontre, Club

inverted_mapping = {1: 'AC AJACCIO',
 2: 'AJ AUXERRE',
 3: 'ANGERS SCO',
 4: 'AS MONACO',
 5: 'CLERMONT FOOT 63',
 6: 'ESTAC TROYES',
 7: 'FC LORIENT',
 8: 'FC NANTES',
 9: 'LOSC LILLE',
 10: 'MONTPELLIER HERAULT SC',
 11: 'OGC NICE',
 12: 'OLYMPIQUE DE MARSEILLE',
 13: 'OLYMPIQUE LYONNAIS',
 14: 'PARIS SAINT-GERMAIN',
 15: 'RC LENS',
 16: 'RC STRASBOURG ALSACE',
 17: 'STADE BRESTOIS 29',
 18: 'STADE DE REIMS',
 19: 'STADE RENNAIS FC',
 20: 'TOULOUSE FC'}

def get_ranking_template():
    ranking_temp = {}
    for key in mapping.keys():
        ranking_temp[key] = {"logo" : Club.objects.get(nom=key).logo,
                             "nb_pts": 0, 
                         "joué":0, 
                         "gagné" :0, 
                         "perdu" :0, 
                         "nul" :0, 
                         "buts_mis": 0,
                         "buts_pris":0,
                         "diff": 0}
    return ranking_temp

def get_score(team_name : str, ranking_temp : dict, rencontre: dict or Rencontre): 
    if inverted_mapping.get(int(rencontre["equipe_dom_id"])) == team_name:
        ranking_temp[team_name]["buts_mis"] += rencontre['buts_dom']
        ranking_temp[team_name]["buts_pris"] += rencontre['buts_vis']
        if rencontre['buts_dom'] > rencontre['buts_vis'] :
            ranking_temp[team_name]["nb_pts"] += 3
            ranking_temp[team_name]["gagné"] += 1
        elif rencontre['buts_dom'] < rencontre['buts_vis'] :
            ranking_temp[team_name]["perdu"] += 1
        elif rencontre['buts_dom'] == rencontre['buts_vis']:
            ranking_temp[team_name]["nb_pts"] += 1
            ranking_temp[team_name]["nul"] += 1
    elif inverted_mapping.get(int(rencontre["equipe_vis_id"])) == team_name:
        ranking_temp[team_name]["buts_mis"] += rencontre['buts_vis']
        ranking_temp[team_name]["buts_pris"] += rencontre['buts_dom']
        if rencontre['buts_dom'] < rencontre['buts_vis'] :
            ranking_temp[team_name]["nb_pts"] += 3
            ranking_temp[team_name]["gagné"] += 1
        elif rencontre['buts_dom'] > rencontre['buts_vis'] :
            ranking_temp[team_name]["perdu"] += 1
        elif rencontre['buts_dom'] == rencontre['buts_vis']:
            ranking_temp[team_name]["nb_pts"] += 1
            ranking_temp[team_name]["nul"] += 1
    