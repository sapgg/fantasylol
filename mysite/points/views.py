import time

from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from .forms import PointForm
from pyriot.wrapper import PyRiot, NORTH_AMERICA
from pyriot.riot import split_teams, get_summoner_pts, get_summoner_names

API_KEY = 'a22e3d70-3a1d-4b70-8563-005066d86de6'
summoner_name = ""

# Create your views here.
def home(request):
    form = PointForm(request.POST or None)

    if form.is_valid():
        global summoner_name
        summoner_name = form.cleaned_data['summoner_name']

        #save_it = form.save(commit=False)
        #save_it.save()

        #### NEED TO FIGURE OUT HOW TO PASS ARGUMENTS THROUGH HttpResponseRedirect
        #### so we don't need to use global variable
        return HttpResponseRedirect('/search/')
    else:
        return render_to_response("point.html",
                              locals(),
                              context_instance=RequestContext(request))


def search(request):
    # process summoner name
    global summoner_name
    class Info(object):
        def __init__(self, name, champion, points):
            self.name = name
            self.champion = champion
            self.points = points

    priot = PyRiot(API_KEY)
    champions = priot.static_champions(NORTH_AMERICA)

    summoner = priot.summoner_get_by_name(NORTH_AMERICA, summoner_name.lower())
    last_game = priot.recent_games(NORTH_AMERICA, summoner.id)[0]
    summoners_champ = champions[last_game.champion_id]
    fellow_players = last_game.fellow_players
    summoner_names = get_summoner_names(priot, fellow_players)
    my_team, enemy_team = split_teams(fellow_players, last_game.team_id)

    ally_data = [Info(summoner_name,
            summoners_champ.name,
            get_summoner_pts(priot, summoner.id, last_game.game_id))]
    for player in my_team:
        ally_data.append(Info(summoner_names[player.summoner_id],
                         champions[player.champion_id].name,
                         get_summoner_pts(priot, player.summoner_id, last_game.game_id)))

    ally_total = 0
    for member in ally_data:
        if member.points != -100:
            ally_total += member.points

    time.sleep(10)

    enemy_data = []
    for player in enemy_team:
        enemy_data.append(Info(summoner_names[player.summoner_id],
                         champions[player.champion_id].name,
                         get_summoner_pts(priot, player.summoner_id, last_game.game_id)))

    enemy_total = 0
    for enemy in enemy_data:
        if enemy.points != -100:
            enemy_total += enemy.points

    return render_to_response(  "search.html",
                                {   "summoner_name": summoner_name,
                                    "ally_data": ally_data,
                                    "ally_total": ally_total,
                                    "enemy_data": enemy_data,
                                    "enemy_total": enemy_total      },
                                context_instance=RequestContext(request))