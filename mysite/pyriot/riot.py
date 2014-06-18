from wrapper import NORTH_AMERICA

#API_KEY = 'a22e3d70-3a1d-4b70-8563-005066d86de6'


class SummGameInfo(object):
    def __init__(self):
        self.name = ""
        self.champion = ""
        self.fantasy_points = 0
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.creep_score = 0
        self.triples = 0
        self.quadras = 0
        self.pentas = 0
        self.bonus = 0

    def set_name_champ(self, name, champ):
        self.name = name
        self.champion = champ

    def calc_fantasy_pts(self):
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
        if self.fantasy_points == -100:
            return
        fantasy_pts = 0
        fantasy_pts += 2 * self.kills
        fantasy_pts -= 0.5 * self.deaths
        fantasy_pts += 1.5 * self.assists
        fantasy_pts += 0.01 * self.creep_score
        fantasy_pts += 2 * self.triples
        fantasy_pts += 5 * self.quadras
        fantasy_pts += 10 * self.pentas
        fantasy_pts += self.bonus
        self.fantasy_points = fantasy_pts

    def __object_string(self):
        objdict = self.__dict__
        object_string = ''
        for key in objdict:
            object_string = object_string + '{0}: {1}\n'.format(key, objdict[key])

        return object_string

    def __repr__(self):
        return self.__object_string()

    def __str__(self):
        return self.__object_string()

    def __unicode__(self):
        return self.__object_string()


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


def get_summ_info(priot, summoner_id, game_id):

    recent_games = priot.recent_games(NORTH_AMERICA, summoner_id)
    relevant_game = 0
    for game in recent_games:
        if game.game_id == game_id:
            relevant_game = game

    summ_info = SummGameInfo()
    if relevant_game == 0:
        summ_info.fantasy_points = -100
        return summ_info

    if hasattr(relevant_game.stats, 'champions_killed'):
        summ_info.kills = relevant_game.stats.champions_killed
    if hasattr(relevant_game.stats, 'num_deaths'):
        summ_info.deaths = relevant_game.stats.num_deaths
    if hasattr(relevant_game.stats, 'assists'):
        summ_info.assists = relevant_game.stats.assists
    if hasattr(relevant_game.stats, 'minions_killed'):
        summ_info.creep_score = relevant_game.stats.minions_killed
    if hasattr(relevant_game.stats, 'neutral_minions_killed'):
        summ_info.creep_score += relevant_game.stats.neutral_minions_killed
    if hasattr(relevant_game.stats, 'triple_kills'):
        summ_info.triples = relevant_game.stats.triple_kills
    if hasattr(relevant_game.stats, 'quadra_kills'):
        summ_info.quadras = relevant_game.stats.quadra_kills
    if hasattr(relevant_game.stats, 'penta_kills'):
        summ_info.pentas = relevant_game.stats.penta_kills
    if summ_info.kills + summ_info.assists >= 10:
        summ_info.bonus = 2
    return summ_info


def calc_totals(data):
    totals_info = SummGameInfo()
    for summoner in data:
        totals_info.kills += summoner.kills
        totals_info.deaths += summoner.deaths
        totals_info.assists += summoner.assists
        totals_info.creep_score += summoner.creep_score
        totals_info.triples += summoner.triples
        totals_info.quadras += summoner.quadras
        totals_info.pentas += summoner.pentas
        totals_info.bonus += summoner.bonus
    totals_info.calc_fantasy_pts()
    return totals_info

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
