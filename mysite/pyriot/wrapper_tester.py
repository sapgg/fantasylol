import time

from wrapper import PyRiot, NORTH_AMERICA


API_KEY = 'a22e3d70-3a1d-4b70-8563-005066d86de6'

priot = PyRiot(API_KEY)

summoner_name = raw_input('\nPlease enter a summoner name: ')

# PyRiot.champions
test_champions = priot.champions(NORTH_AMERICA)
print test_champions

# PyRiot.static_champions
test_static_champions = priot.static_champions(NORTH_AMERICA)
print test_static_champions


# PyRiot.summoner_get_by_name
summoner = priot.summoner_get_by_name(NORTH_AMERICA, summoner_name.lower())

"""
# PyRiot.leagues
test_leagues = priot.leagues(NORTH_AMERICA, summoner.id)
print test_leagues
"""

# PyRiot.recent_games
test_recent_games = priot.recent_games(NORTH_AMERICA, summoner.id)
print test_recent_games

# PyRiot.summoner_get_by_id
test_summoner_get_by_id = priot.summoner_get_by_id(NORTH_AMERICA, summoner.id)
print test_summoner_get_by_id

# PyRiot.stats_summary
test_stats_summary = priot.stats_summary(NORTH_AMERICA, summoner.id, 4)
print test_stats_summary

# PyRiot.stats_ranked
test_stats_ranked = priot.stats_ranked(NORTH_AMERICA, summoner.id, 4)
print test_stats_ranked

# PyRiot.summoner_masteries
test_summoner_masteries = priot.summoner_masteries(NORTH_AMERICA, summoner.id)
print test_summoner_masteries

# PyRiot.summoner_runes
test_summoner_runes = priot.summoner_runes(NORTH_AMERICA, summoner.id)
print test_summoner_runes

time.sleep(10)


# PyRiot.summoner_get_names_for_ids
id_1 = (priot.summoner_get_by_name(NORTH_AMERICA, "w1ngw")).id
id_2 = (priot.summoner_get_by_name(NORTH_AMERICA, "scatteringeffect")).id
test_summoner_get_names_for_ids = priot.summoner_get_names_for_ids(NORTH_AMERICA, str(id_1) + "," + str(id_2))
print test_summoner_get_names_for_ids

# PyRiot.teams
test_teams = priot.teams(NORTH_AMERICA, summoner.id)
print test_teams
