from wrapper import NORTH_AMERICA

#API_KEY = 'a22e3d70-3a1d-4b70-8563-005066d86de6'

def split_teams(fellow_players, my_team_id):
    my_team = []
    enemy_team = []
    for player in fellow_players:
        if player.team_id == my_team_id:
            my_team.append(player)
        else:
            enemy_team.append(player)
    return my_team, enemy_team

def get_summoner_names(priot, players):
    player_ids = ''
    summoners = dict()
    for player in players:
        player_ids += str(player.summoner_id)
        player_ids += ','
    name_dict = priot.summoner_get_names_for_ids('na', player_ids)
    for id_str in name_dict:
        summoners[int(id_str)] = name_dict[id_str]
    return summoners

def get_summoner_pts(priot, summoner_id, game_id):
    """
    Player Score:
    Kills      2    pts
    Deaths    -0.5  pts
    Assists    1.5  pts
    CS         0.01 pts
    Triple     2 Bonus pts
    Quadra     5 Bonus pts
    Penta     10 Bonus pts
    10+ K/A    2 Bonus pts
    """
    fantasy_pts = 0
    recent_games = priot.recent_games(NORTH_AMERICA, summoner_id)
    relevant_game = 0
    for game in recent_games:
        if game.game_id == game_id:
            relevant_game = game
    if relevant_game == 0:
        return -100

    kills = assists = 0
    if hasattr(relevant_game.stats, 'champions_killed'):
        kills = relevant_game.stats.champions_killed
        fantasy_pts += 2 * kills
    if hasattr(relevant_game.stats, 'num_deaths'):
        fantasy_pts -= 0.5 * relevant_game.stats.num_deaths
    if hasattr(relevant_game.stats, 'assists'):
        assists = relevant_game.stats.assists
        fantasy_pts += 1.5 * assists
    if hasattr(relevant_game.stats, 'minions_killed'):
        fantasy_pts += 0.01 * relevant_game.stats.minions_killed
    if hasattr(relevant_game.stats, 'neutral_minions_killed'):
        fantasy_pts += 0.01 * relevant_game.stats.neutral_minions_killed
    if hasattr(relevant_game.stats, 'triple_kills'):
        fantasy_pts += 2 * relevant_game.stats.triple_kills
    if hasattr(relevant_game.stats, 'quadra_kills'):
        fantasy_pts += 5 * relevant_game.stats.quadra_kills
    if hasattr(relevant_game.stats, 'penta_kills'):
        fantasy_pts += 10 * relevant_game.stats.penta_kills
    if kills+assists >= 10:
        fantasy_pts += 2
    return fantasy_pts


"""
priot = PyRiot(API_KEY)
champions = priot.static_champions(NORTH_AMERICA)

# SUMMONER_URL = 'https://prod.api.pvp.net/api/lol/na/v1.3/summoner/by-name/{}?api_key={}'
# r = requests.get(SUMMONER_URL.format(SUMMONER, API_KEY))
# print r


while True:

    summoner_name = raw_input('\nPlease enter a summoner name: ')
    #summoner_name = 'w1ngw'
    try:
        summoner = priot.summoner_get_by_name(NORTH_AMERICA, summoner_name.lower())
    except TypeError as e:
        print("Error. {} could not be found. (Riot's API seems to be case sensitive...".format(summoner_name))
        continue

    #leagues = priot.leagues(NORTH_AMERICA, summoner.id)

    last_game = priot.recent_games(NORTH_AMERICA, summoner.id)[0]
    summoners_champ = champions[last_game.champion_id]
    fellow_players = last_game.fellow_players
    my_team, enemy_team = split_teams(fellow_players, last_game.team_id)
    print("In {}'s last game, the team comps were:".format(summoner_name))
    print('----------------------------------------------')
    player_fantasy_pts = get_summoner_pts(summoner.id, last_game.game_id)
    print("{} | {} | {:>7,.2f}".format(summoner_name.ljust(18), summoners_champ.name.ljust(13), player_fantasy_pts))
    summoner_names = get_summoner_names(fellow_players)
    for player in my_team:
        player_name = summoner_names[player.summoner_id]
        player_champ = champions[player.champion_id]
        player_fantasy_pts = get_summoner_pts(player.summoner_id, last_game.game_id)
        print("{} | {} | {:>7,.2f}".format(player_name.encode('utf8').ljust(18), player_champ.name.ljust(13), player_fantasy_pts))
    print('----------------------VS----------------------')
    time.sleep(10)
    for player in enemy_team:
        player_name = summoner_names[player.summoner_id]
        player_champ = champions[player.champion_id]
        player_fantasy_pts = get_summoner_pts(player.summoner_id, last_game.game_id)
        print("{} | {} | {:>7,.2f}".format(player_name.encode('utf8').ljust(18), player_champ.name.ljust(13), player_fantasy_pts))
    print('----------------------------------------------')

"""
