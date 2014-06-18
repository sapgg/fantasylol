import time

from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from .forms import PlayerForm
from pyriot.wrapper import PyRiot, NORTH_AMERICA
from pyriot.riot import split_teams, get_summ_info, get_summoner_names, calc_totals, SummGameInfo

API_KEY = 'a22e3d70-3a1d-4b70-8563-005066d86de6'
summoner_name = ""

# Create your views here.
def home(request):
    form = PlayerForm(request.POST or None)

    if form.is_valid():
        global summoner_name
        summoner_name = (form.cleaned_data['summoner_name']).replace(" ", "")

        #save_it = form.save(commit=False)
        #save_it.save()

        #### NEED TO FIGURE OUT HOW TO PASS ARGUMENTS THROUGH HttpResponseRedirect
        #### so we don't need to use global variable
        return HttpResponseRedirect('/search/')
    else:
        return render_to_response("homepage.html",
                              locals(),
                              context_instance=RequestContext(request))


def search(request):
    # process summoner name
    global summoner_name

    priot = PyRiot(API_KEY)
    champions = priot.static_champions(NORTH_AMERICA)
    #try:
    summoner = priot.summoner_get_by_name(NORTH_AMERICA, summoner_name.lower())
    last_game = priot.recent_games(NORTH_AMERICA, summoner.id)[0]
    summoners_champ = champions[last_game.champion_id]
    fellow_players = last_game.fellow_players
    summoner_names = get_summoner_names(priot, fellow_players)
    my_team, enemy_team = split_teams(fellow_players, last_game.team_id)

    summ_info = get_summ_info(priot, summoner.id, last_game.game_id)
    summ_info.calc_fantasy_pts()
    summ_info.name = summoner_name
    summ_info.champion = summoners_champ.name
    ally_data = [summ_info]

    for player in my_team:
        summ_info = get_summ_info(priot, player.summoner_id, last_game.game_id)
        print summ_info
        summ_info.set_name_champ(summoner_names[player.summoner_id], champions[player.champion_id].name)
        summ_info.calc_fantasy_pts()
        ally_data.append(summ_info)

    time.sleep(10)

    enemy_data = []
    for player in enemy_team:
        summ_info = SummGameInfo()
        summ_info = get_summ_info(priot, player.summoner_id, last_game.game_id)

        summ_info.name = summoner_names[player.summoner_id]
        summ_info.champion = champions[player.champion_id].name
        summ_info.calc_fantasy_pts()
        enemy_data.append(summ_info)

    ally_totals_info = calc_totals(ally_data)
    ally_totals_info.name = "Allied Team Totals"
    ally_data.append(ally_totals_info)
    enemy_totals_info = calc_totals(enemy_data)
    enemy_totals_info.name = "Enemy Team Totals"
    enemy_data.append(enemy_totals_info)

    return render_to_response("search.html",
                                {"summoner_name": summoner_name,
                                "ally_data": ally_data,
                                "ally_totals_info": ally_totals_info,
                                "enemy_data": enemy_data,
                                "enemy_totals_info": enemy_totals_info},
                                context_instance=RequestContext(request))

    """
    except Exception as e:
        #TODO: Catch the correct exception. We don't want to do this for EVERY exception.
        return render_to_response("invalid_summoner_error.html",
                                  {"summoner_name": summoner_name},
                                  context_instance=RequestContext(request))
    """

def about(request):
    return render_to_response("about.html",
                              locals(),
                              context_instance=RequestContext(request))