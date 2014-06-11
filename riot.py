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

def get_summoner_pts(summoner_id, game_id):
    fantasy_pts = 0
    recent_games = priot.recent_games(NORTH_AMERICA, summoner_id)
    relevant_game = 0
    for game in recent_games:
        if game.game_id == game_id:
            relevant_game = game
    if relevant_game == 0:
        return -1
    kills = deaths = assists = creep_score = triples = quadras = pentas = bonus = 0
    if 'championsKilled' in relevant_game.stats:
        kills = relevant_game.stats['championsKilled']
    if 'numDeaths' in relevant_game.stats:
        deaths = relevant_game.stats['numDeaths']
    if 'assists' in relevant_game.stats:
        assists = relevant_game.stats['assists']
    if 'minionsKilled' in relevant_game.stats:
        creep_score = relevant_game.stats['minionsKilled']
    if 'neutralMinionsKilled' in relevant_game.stats:
        creep_score += relevant_game.stats['neutralMinionsKilled']
    if 'tripleKills' in relevant_game.stats:
        triples = relevant_game.stats['tripleKills']
    if 'quadraKills' in relevant_game.stats:
        quadras = relevant_game.stats['quadraKills']
    if 'pentaKills' in relevant_game.stats:
        pentas = relevant_game.stats['pentaKills']
    if kills+deaths >= 10:
        bonus = 2
    fantasy_pts = 2*kills - 0.5*deaths + 1.5*assists + 0.01*creep_score + \
        2*triples + 5*quadras + 10*pentas + bonus
    return fantasy_pts




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
    player_fantasy_pts = get_summoner_pts(summoner.id, last_game.game_id)
    print("{} {} {}".format(summoner_name, summoners_champ, player_fantasy_pts))
    summoner_names = get_summoner_names(fellow_players)
    for player in my_team:
        player_name = summoner_names[player.summoner_id]
        player_champ = champions[player.champion_id]
        player_fantasy_pts = get_summoner_pts(player.summoner_id, last_game.game_id)
        print("{} {} {}".format(player_name.encode('utf8'), player_champ, player_fantasy_pts))
    print('------------------VS----------------')
    time.sleep(10)
    for player in enemy_team:
        player_name = summoner_names[player.summoner_id]
        player_champ = champions[player.champion_id]
        player_fantasy_pts = get_summoner_pts(player.summoner_id, last_game.game_id)
        print("{} {} {}".format(player_name.encode('utf8'), player_champ, player_fantasy_pts))
    print('------------------------------------')

