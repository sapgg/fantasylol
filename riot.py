import requests
from pyriot.wrapper import PyRiot, NORTH_AMERICA
import time

API_KEY = 'a22e3d70-3a1d-4b70-8563-005066d86de6'

def static_champions():
    url = 'https://prod.api.pvp.net/api/lol/static-data/na/v1.2/champion?api_key={}'.format(API_KEY)
    response = requests.get(url)
    content = response.json()
    champions = dict()
    for champion in content['data']:
        champions[content['data'][champion]['id']] = champion
    return champions

def split_teams(fellow_players, my_team_id):
    my_team = []
    enemy_team = []
    for player in fellow_players:
        if player.team_id == my_team_id:
            my_team.append(player)
        else:
            enemy_team.append(player)
    return my_team, enemy_team

def get_summoner_names(players):
    player_ids = ''
    summoners = dict()
    for player in players:
        player_ids += str(player.summoner_id)
        player_ids += ','
    name_dict = priot.summoner_get_names_for_ids('na', player_ids)
    for id_str in name_dict:
        summoners[int(id_str)] = name_dict[id_str]
    return summoners

champions = static_champions()
# SUMMONER_URL = 'https://prod.api.pvp.net/api/lol/na/v1.3/summoner/by-name/{}?api_key={}'
# r = requests.get(SUMMONER_URL.format(SUMMONER, API_KEY))
# print r
while True:
    summoner_name = raw_input('\nPlease enter a summoner name: ')
    #summoner_name = 'w1ngw'
    priot = PyRiot(API_KEY)
    try:
        summoner = priot.summoner_get_by_name(NORTH_AMERICA, summoner_name)
    except TypeError as e:
        print("Error. {} could not be found. (Riot's API seems to be case sensitive...".format(summoner_name))
        continue
    last_game = priot.recent_games(NORTH_AMERICA, summoner.id)[0]
    summoners_champ = champions[last_game.champion_id]
    fellow_players = last_game.fellow_players
    my_team, enemy_team = split_teams(fellow_players, last_game.team_id)
    print("In {}'s last game, the team comps were:".format(summoner_name))
    print('------------------------------------')
    print("{} {}".format(summoner_name, summoners_champ))
    summoner_names = get_summoner_names(fellow_players)
    for player in my_team:
        player_name = summoner_names[player.summoner_id]
        player_champ = champions[player.champion_id]
        print("{} {}".format(player_name.encode('utf8'), player_champ))
    print('------------------VS----------------')
    for player in enemy_team:
        player_name = summoner_names[player.summoner_id]
        player_champ = champions[player.champion_id]
        print("{} {}".format(player_name.encode('utf8'), player_champ))
    print('------------------------------------')

