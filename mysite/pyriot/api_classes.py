# -*- coding: utf-8 -*-

import sys

import utils

reload(sys)
sys.setdefaultencoding("utf-8")


class Summoner(object):
    """
    id              long        Summoner ID.
    name            string      Summoner name.
    profileIconId   int         ID of the summoner icon associated with the summoner.
    revisionDate    long        Date summoner was last modified specified as epoch milliseconds.
    summonerLevel   long        Summoner level associated with the summoner.
    """
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.profile_icon_id = kwargs['profileIconId']
        self.revision_date = utils.convert_epoch_millis_to_datetime(kwargs['revisionDate'])
        self.summoner_level = kwargs['summonerLevel']

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


class Champion(object):
    """
    active              boolean     Indicates if the champion is active.
    attackRank          int         Champion attack rank.
    botEnabled          boolean     Bot enabled flag (for custom games).
    botMmEnabled        boolean     Bot Match Made enabled flag (for Co-op vs. AI games).
    defenseRank         int         Champion defense rank.
    difficultyRank      int         Champion difficulty rank.
    freeToPlay          boolean     Indicates if the champion is free to play. Free to play champions are rotated periodically.
    id                  long        Champion ID.
    magicRank           int         Champion magic rank.
    name                string      Champion name.
    rankedPlayEnabled   boolean     Ranked play enabled flag.
    """
    def __init__(self, **kwargs):
        self.active = kwargs['active']
        #self.attack_rank = kwargs['attackRank']
        self.bot_enabled = kwargs['botEnabled']
        self.bot_mm_enabled = kwargs['botMmEnabled']
        #self.defense_rank = kwargs['defenseRank']
        #self.difficulty_rank = kwargs['difficultyRank']
        self.free_to_play = kwargs['freeToPlay']
        self.id = kwargs['id']
        #self.magic_rank = kwargs['magicRank']
        #self.name = kwargs['name']
        self.ranked_play_enabled = kwargs['rankedPlayEnabled']

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


class Game(object):
    """
    championId      int                 Champion ID associated with game.
    createDate      long                Date that end game data was recorded, specified as epoch milliseconds.
    fellowPlayers   List[PlayerDto]     Other players associated with the game.
    gameId          long                Game ID.
    gameMode        string              Game mode.
    gameType        string              Game type.
    invalid         boolean             Invalid flag.
    level           int                 Level.
    mapId           int                 Map ID.
    spell1          int                 ID of first summoner spell.
    spell2          int                 ID of second summoner spell.
    stats	        RawStatsDto	        Statistics associated with the game for this summoner.
    subType         string              Game sub-type.
    teamId          int                 Team ID associated with game.
    """
    def __init__(self, **kwargs):
        self.champion_id = kwargs['championId']
        self.create_date = utils.convert_epoch_millis_to_datetime(kwargs['createDate'])

        players = []
        try:
            for player in kwargs['fellowPlayers']:
                players.append(Player(**player))
        except KeyError:
            pass
        self.fellow_players = players

        self.game_id = kwargs['gameId']
        self.game_mode = kwargs['gameMode']
        self.game_type = kwargs['gameType']
        self.invalid = kwargs['invalid']
        self.level = kwargs['level']
        self.map_id = kwargs['mapId']
        self.spell1 = kwargs['spell1']
        self.spell2 = kwargs['spell2']
        self.stats = RawStat(**kwargs['stats'])
        self.sub_type = kwargs['subType']
        self.team_id = kwargs['teamId']

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


class Player(object):
    """
    championId  int     Champion id associated with player.
    summonerId  long    Summoner id associated with player.
    teamId      int     Team id associated with player.
    """
    def __init__(self, **kwargs):
        self.champion_id = kwargs['championId']
        self.summoner_id = kwargs['summonerId']
        self.team_id = kwargs['teamId']

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


class RawStat(object):
    """
    assists	                int
    barracksKilled	        int	Number of enemy inhibitors killed.
    championsKilled	        int
    combatPlayerScore	    int
    consumablesPurchased	int
    damageDealtPlayer	    int
    doubleKills	            int
    firstBlood	            int
    gold	                int
    goldEarned	            int
    goldSpent	            int
    item0	                int
    item1	                int
    item2	                int
    item3	                int
    item4	                int
    item5	                int
    item6	                int
    itemsPurchased	        int
    killingSprees	        int
    largestCriticalStrike	    int
    largestKillingSpree	        int
    largestMultiKill	        int
    legendaryItemsCreated	    int	Number of tier 3 items built.
    level	                    int
    magicDamageDealtPlayer	    int
    magicDamageDealtToChampions	int
    magicDamageTaken	        int
    minionsDenied	            int
    minionsKilled	            int
    neutralMinionsKilled	    int
    neutralMinionsKilledEnemyJungle	int
    neutralMinionsKilledYourJungle	int
    nexusKilled	            boolean	Flag specifying if the summoner got the killing blow on the nexus.
    nodeCapture	            int
    nodeCaptureAssist	    int
    nodeNeutralize	        int
    nodeNeutralizeAssist	int
    numDeaths	            int
    numItemsBought	        int
    objectivePlayerScore	int
    pentaKills	            int
    physicalDamageDealtPlayer	    int
    physicalDamageDealtToChampions	int
    physicalDamageTaken	int
    quadraKills	        int
    sightWardsBought	int
    spell1Cast	        int	Number of times first champion spell was cast.
    spell2Cast	        int	Number of times second champion spell was cast.
    spell3Cast	        int	Number of times third champion spell was cast.
    spell4Cast	        int	Number of times fourth champion spell was cast.
    summonSpell1Cast	int
    summonSpell2Cast	int
    superMonsterKilled	int
    team	            int
    teamObjective	    int
    timePlayed	        int
    totalDamageDealt	int
    totalDamageDealtToChampions	int
    totalDamageTaken	int
    totalHeal	        int
    totalPlayerScore	int
    totalScoreRank	    int
    totalTimeCrowdControlDealt	int
    totalUnitsHealed	int
    tripleKills	        int
    trueDamageDealtPlayer	int
    trueDamageDealtToChampions	int
    trueDamageTaken	    int
    turretsKilled	    int
    unrealKills	        int
    victoryPointTotal	int
    visionWardsBought	int
    wardKilled	        int
    wardPlaced	        int
    win	                boolean	Flag specifying whether or not this game was won.
    """

    def __init__(self, **kwargs):
        if 'assists' in kwargs:
            self.assists = kwargs['assists']
        if 'barracksKilled' in kwargs:
            self.barracks_killed = kwargs['barracksKilled']
        if 'championsKilled' in kwargs:
            self.champions_killed = kwargs['championsKilled']
        if 'combatPlayerScore' in kwargs:
            self.combat_player_score = kwargs['combatPlayerScore']
        if 'consumablesPurchased' in kwargs:
            self.consumables_purchased = kwargs['consumablesPurchased']
        if 'damageDealtPlayer' in kwargs:
            self.damage_dealt_player = kwargs['damageDealtPlayer']
        if 'doubleKills' in kwargs:
            self.double_kills = kwargs['doubleKills']
        if 'firstBlood' in kwargs:
            self.first_blood = kwargs['firstBlood']
        if 'gold' in kwargs:
            self.gold = kwargs['gold']
        if 'goldEarned' in kwargs:
            self.gold_earned = kwargs['goldEarned']
        if 'goldSpent' in kwargs:
            self.gold_spent = kwargs['goldSpent']
        if 'item0' in kwargs:
            self.item_0 = kwargs['item0']
        if 'item1' in kwargs:
            self.item_1 = kwargs['item1']
        if 'item2' in kwargs:
            self.item_2 = kwargs['item2']
        if 'item3' in kwargs:
            self.item_3 = kwargs['item3']
        if 'item4' in kwargs:
            self.item_4 = kwargs['item4']
        if 'item5' in kwargs:
            self.item_5 = kwargs['item5']
        if 'item6' in kwargs:
            self.item_6 = kwargs['item6']
        if 'itemsPurchased' in kwargs:
            self.items_purchased = kwargs['itemsPurchased']
        if 'killingSprees' in kwargs:
            self.killing_sprees = kwargs['killingSprees']
        if 'largestCriticalStrike' in kwargs:
            self.largest_critical_strike = kwargs['largestCriticalStrike']
        if 'largestKillingSpree' in kwargs:
            self.largest_killing_spree = kwargs['largestKillingSpree']
        if 'largestMultiKill' in kwargs:
            self.largest_multi_kill = kwargs['largestMultiKill']
        if 'legendaryItemsCreated' in kwargs:
            self.legendary_items_created = kwargs['legendaryItemsCreated']
        if 'level' in kwargs:
            self.level = kwargs['level']
        if 'magicDamageDealtPlayer' in kwargs:
            self.magic_damage_dealt_player = kwargs['magicDamageDealtPlayer']
        if 'magicDamageDealtToChampions' in kwargs:
            self.magic_damage_dealt_to_champions = kwargs['magicDamageDealtToChampions']
        if 'magicDamageTaken' in kwargs:
            self.magic_damage_taken = kwargs['magicDamageTaken']
        if 'minionsDenied' in kwargs:
            self.minions_denied = kwargs['minionsDenied']
        if 'minionsKilled' in kwargs:
            self.minions_killed = kwargs['minionsKilled']
        if 'neutralMinionsKilled' in kwargs:
            self.neutral_minions_killed = kwargs['neutralMinionsKilled']
        if 'neutralMinionsKilledEnemyJungle' in kwargs:
            self.neutral_minions_killed_enemy_jungle = kwargs['neutralMinionsKilledEnemyJungle']
        if 'neutralMinionsKilledYourJungle' in kwargs:
            self.neutral_minions_killed_your_jungle = kwargs['neutralMinionsKilledYourJungle']
        if 'nexusKilled' in kwargs:
            self.nexus_killed = kwargs['nexusKilled']
        if 'nodeCapture' in kwargs:
            self.node_capture = kwargs['nodeCapture']
        if 'nodeCaptureAssist' in kwargs:
            self.node_capture_assist = kwargs['nodeCaptureAssist']
        if 'nodeNeutralize' in kwargs:
            self.node_neutralize = kwargs['nodeNeutralize']
        if 'nodeNeutralizeAssist' in kwargs:
            self.node_neutralize_assist = kwargs['nodeNeutralizeAssist']
        if 'numDeaths' in kwargs:
            self.num_deaths = kwargs['numDeaths']
        if 'numItemsBought' in kwargs:
            self.num_items_bought = kwargs['numItemsBought']
        if 'objectivePlayerScore' in kwargs:
            self.objective_player_score = kwargs['objectivePlayerScore']
        if 'pentaKills' in kwargs:
            self.penta_kills = kwargs['pentaKills']
        if 'physicalDamageDealtPlayer' in kwargs:
            self.physical_damage_dealt_player = kwargs['physicalDamageDealtPlayer']
        if 'physicalDamageDealtToChampions' in kwargs:
            self.physical_damage_dealt_to_champions = kwargs['physicalDamageDealtToChampions']
        if 'PhysicalDamageTaken' in kwargs:
            self.physical_damage_taken = kwargs['PhysicalDamageTaken']
        if 'quadraKills' in kwargs:
            self.quadra_kills = kwargs['quadraKills']
        if 'sightWardsBought' in kwargs:
            self.sight_wards_bought = kwargs['sightWardsBought']
        if 'spell1Cast' in kwargs:
            self.spell_1_cast = kwargs['spell1Cast']
        if 'spell2Cast' in kwargs:
            self.spell_2_cast = kwargs['spell2Cast']
        if 'spell3Cast' in kwargs:
            self.spell_3_cast = kwargs['spell3Cast']
        if 'spell4Cast' in kwargs:
            self.spell_4_cast = kwargs['spell4Cast']
        if 'summonSpell1Cast' in kwargs:
            self.summon_spell_1_cast = kwargs['summonSpell1Cast']
        if 'summonSpell2Cast' in kwargs:
            self.sumon_spell_2_cast = kwargs['summonSpell2Cast']
        if 'superMonsterKilled' in kwargs:
            self.super_monster_killed = kwargs['superMonsterKilled']
        if 'team' in kwargs:
            self.team = kwargs['team']
        if 'teamObjective' in kwargs:
            self.team_objective = kwargs['teamObjective']
        if 'timePlayed' in kwargs:
            self.time_played = kwargs['timePlayed']
        if 'totalDamageDealt' in kwargs:
            self.total_damage_dealt = kwargs['totalDamageDealt']
        if 'totalDamageDealtToChampions' in kwargs:
            self.total_damage_dealt_to_champions = kwargs['totalDamageDealtToChampions']
        if 'totalDamageTaken' in kwargs:
            self.total_damage_taken = kwargs['totalDamageTaken']
        if 'totalHeal' in kwargs:
            self.total_heal = kwargs['totalHeal']
        if 'totalPlayerScore' in kwargs:
            self.total_player_score = kwargs['totalPlayerScore']
        if 'totalScoreRank' in kwargs:
            self.total_score_rank = kwargs['totalScoreRank']
        if 'totalTimeCrowdControlDealt' in kwargs:
            self.total_time_crowd_control_dealt = kwargs['totalTimeCrowdControlDealt']
        if 'totalUnitsHealed' in kwargs:
            self.total_units_healed = kwargs['totalUnitsHealed']
        if 'tripleKills' in kwargs:
            self.triple_kills = kwargs['tripleKills']
        if 'trueDamageTaken' in kwargs:
            self.true_damage_taken = kwargs['trueDamageTaken']
        if 'turretsKilled' in kwargs:
            self.turrets_killed = kwargs['turretsKilled']
        if 'unrealKills' in kwargs:
            self.unreal_kills = kwargs['unrealKills']
        if 'victoryPointTotal' in kwargs:
            self.victory_point_total = kwargs['victoryPointTotal']
        if 'visionWardsBought' in kwargs:
            self.vision_wards_bought = kwargs['visionWardsBought']
        if 'wardKilled' in kwargs:
            self.ward_killed = kwargs['wardKilled']
        if 'wardPlaced' in kwargs:
            self.ward_placed = kwargs['wardPlaced']
        if 'win' in kwargs:
            self.win = kwargs['win']

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


class League(object):
    """
    entries     List[LeagueItemDto] 
    name        string  
    queue       string                  (legal values: RANKED_SOLO_5x5, RANKED_TEAM_3x3, RANKED_TEAM_5x5)
    tier        string                  (legal values: CHALLENGER, DIAMOND, PLATINUM, GOLD, SILVER, BRONZE)
    """
    def __init__(self, **kwargs):
        entries = []
        for entry in kwargs['entries']:
            entries.append(LeagueEntry(**entry))
        self.entries = entries

        self.name = kwargs['name']
        self.queue = kwargs['queue']
        self.tier = kwargs['tier']

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


class LeagueEntry(object):
    """
    isFreshBlood        boolean 
    isHotStreak         boolean 
    isInactive          boolean 
    isVeteran           boolean 
    lastPlayed          long    
    leagueName          string  
    leaguePoints        int 
    miniSeries          MiniSeriesDto   
    playerOrTeamId      string  
    playerOrTeamName    string  
    queueType           string  
    rank                string  
    tier                string  
    wins                int
    """
    def __init__(self, **kwargs):
        self.division = kwargs['division']
        self.is_fresh_blood = kwargs['isFreshBlood']
        self.is_hot_streak = kwargs['isHotStreak']
        self.is_inactive = kwargs['isInactive']
        self.is_veteran = kwargs['isVeteran']
        self.league_points = kwargs['leaguePoints']

        if 'miniSeries' in kwargs:
            self.mini_series = MiniSeries(**kwargs['miniSeries'])

        self.player_or_team_id = kwargs['playerOrTeamId']
        self.player_or_team_name = kwargs['playerOrTeamName']
        self.wins = kwargs['wins']

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


class MiniSeries(object):
    """
    losses                  int 
    progress                Array[char] 
    target                  int 
    timeLeftToPlayMillis    long    
    wins                    int
    """
    def __init__(self, **kwargs):
        self.losses = kwargs['losses']
        self.progress = kwargs['progress']
        self.target = kwargs['target']
        self.wins = kwargs['wins']

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


class PlayerStatsSummary(object):
    """
    aggregatedStats         AggregatedStatsDto      Aggregated stats.
    losses                  int                     Number of losses for this queue type. Returned for ranked queue types only.
    modifyDate              long                    Date stats were last modified specified as epoch milliseconds.
    playerStatSummaryType   string                  Player stats summary type. (legal values: AramUnranked5x5, CoopVsAI, OdinUnranked, RankedPremade3x3, RankedPremade5x5, RankedSolo5x5, RankedTeam3x3, RankedTeam5x5, Unranked, Unranked3x3, OneForAll5x5, FirstBlood1x1, FirstBlood2x2)
    wins                    int                     Number of wins for this queue type.
    """
    def __init__(self, **kwargs):
        self.aggregated_stats = AggregatedStats(**kwargs['aggregatedStats'])
        if 'losses' in kwargs:
            self.losses = kwargs['losses']
        self.modify_date = utils.convert_epoch_millis_to_datetime(kwargs['modifyDate'])
        self.player_stat_summary_type = kwargs['playerStatSummaryType']
        self.wins = kwargs['wins']

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


class PlayerRankedStats(object):
    """
    champions       List[ChampionStatsDto]      List of aggregated stats summarized by champion.
    modifyDate      long                        Date stats were last modified specified as epoch milliseconds.
    summonerId      long                        Summoner ID.
    """
    def __init__(self, **kwargs):
        champions = []
        for champion in kwargs['champions']:
            champions.append(ChampionStats(**champion))
        self.champions = champions

        self.modify_date = utils.convert_epoch_millis_to_datetime(kwargs['modifyDate'])
        self.summoner_id = kwargs['summonerId']

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


class ChampionStats(object):
    """
    id          int                     Champion id.
    name        string                  Champion name.
    stats       AggregatedStatsDto      Aggregated stats associated with the champion.
    """
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.stats = AggregatedStats(**kwargs['stats'])

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


class AggregatedStats(object):
    """
    averageAssists                  int     Dominion only.
    averageChampionsKilled          int     Dominion only.
    averageCombatPlayerScore        int     Dominion only.
    averageNodeCapture              int     Dominion only.
    averageNodeCaptureAssist        int     Dominion only.
    averageNodeNeutralize           int     Dominion only.
    averageNodeNeutralizeAssist     int     Dominion only.
    averageNumDeaths                int     Dominion only.
    averageObjectivePlayerScore     int     Dominion only.
    averageTeamObjective            int     Dominion only.
    averageTotalPlayerScore         int     Dominion only.
    botGamesPlayed                  int 
    killingSpree                    int 
    maxAssists                      int     Dominion only.
    maxChampionsKilled              int     
    maxCombatPlayerScore            int     Dominion only.
    maxLargestCriticalStrike        int 
    maxLargestKillingSpree          int 
    maxNodeCapture                  int     Dominion only.
    maxNodeCaptureAssist            int     Dominion only.
    maxNodeNeutralize               int     Dominion only.
    maxNodeNeutralizeAssist         int     Dominion only.
    maxObjectivePlayerScore         int     Dominion only.
    maxTeamObjective                int     Dominion only.
    maxTimePlayed                   int 
    maxTimeSpentLiving              int 
    maxTotalPlayerScore             int     Dominion only.
    mostChampionKillsPerSession     int 
    mostSpellsCast                  int 
    normalGamesPlayed               int 
    rankedPremadeGamesPlayed        int 
    rankedSoloGamesPlayed           int 
    totalAssists                    int 
    totalChampionKills              int 
    totalDamageDealt                int 
    totalDamageTaken                int 
    totalDoubleKills                int 
    totalFirstBlood                 int 
    totalGoldEarned                 int 
    totalHeal                       int 
    totalMagicDamageDealt           int 
    totalMinionKills                int 
    totalNeutralMinionsKilled       int 
    totalNodeCapture                int     Dominion only.
    totalNodeNeutralize             int     Dominion only.
    totalPentaKills                 int 
    totalPhysicalDamageDealt        int 
    totalQuadraKills                int 
    totalSessionsLost               int 
    totalSessionsPlayed             int 
    totalSessionsWon                int 
    totalTripleKills                int 
    totalTurretsKilled              int 
    totalUnrealKills                int
    """
    def __init__(self, **kwargs):
        if 'averageAssists' in kwargs:
            self.average_assists = kwargs['averageAssists']
        if 'averageChampionsKilled' in kwargs:
            self.average_champions_killed = kwargs['averageChampionsKilled']
        if 'averageCombatPlayerScore' in kwargs:
            self.average_combat_player_score = kwargs['averageCombatPlayerScore']
        if 'averageNodeCapture' in kwargs:
            self.average_node_capture = kwargs['averageNodeCapture']
        if 'averageNodeCaptureAssist' in kwargs:
            self.average_node_capture_assist = kwargs['averageNodeCaptureAssist']
        if 'averageNodeNeutralize' in kwargs:
            self.average_node_neutralize = kwargs['averageNodeNeutralize']
        if 'averageNodeNeutralizeAssist' in kwargs:
            self.average_node_neutralize_assist = kwargs['averageNodeNeutralizeAssist']
        if 'averageNumDeaths' in kwargs:
            self.average_num_deaths = kwargs['averageNumDeaths']
        if 'averageObjectivePlayerScore' in kwargs:
            self.average_objective_player_score = kwargs['averageObjectivePlayerScore']
        if 'averageTeamObjective' in kwargs:
            self.average_team_objective = kwargs['averageTeamObjective']
        if 'averageTotalPlayerScore' in kwargs:
            self.average_total_player_score = kwargs['averageTotalPlayerScore']
        if 'botGamesPlayed' in kwargs:
            self.bot_games_played = kwargs['botGamesPlayed']
        if 'killingSpree' in kwargs:
            self.killing_spree = kwargs['killingSpree']
        if 'maxAssists' in kwargs:
            self.max_assists = kwargs['maxAssists']
        if 'maxChampionsKilled' in kwargs:
            self.max_champions_killed = kwargs['maxChampionsKilled']
        if 'maxCombatPlayerScore' in kwargs:
            self.max_combat_player_score = kwargs['maxCombatPlayerScore']
        if 'maxLargestCriticalStrike' in kwargs:
            self.max_largest_critical_strike = kwargs['maxLargestCriticalStrike']
        if 'maxLargestKillingSpree' in kwargs:
            self.max_largest_killing_spree = kwargs['maxLargestKillingSpree']
        if 'maxNodeCapture' in kwargs:
            self.max_node_capture = kwargs['maxNodeCapture']
        if 'maxNodeCaptureAssist' in kwargs:
            self.max_node_capture_assist = kwargs['maxNodeCaptureAssist']
        if 'maxNodeNeutralize' in kwargs:
            self.max_node_neutralize = kwargs['maxNodeNeutralize']
        if 'maxNodeNeutralizeAssist' in kwargs:
            self.max_node_neutralize_assist = kwargs['maxNodeNeutralizeAssist']
        if 'maxObjectivePlayerScore' in kwargs:
            self.max_objective_player_score = kwargs['maxObjectivePlayerScore']
        if 'maxTeamObjective' in kwargs:
            self.max_team_objective = kwargs['maxTeamObjective']
        if 'maxTimePlayed' in kwargs:
            self.max_time_played = kwargs['maxTimePlayed']
        if 'maxTimeSpentLiving' in kwargs:
            self.max_time_spent_living = kwargs['maxTimeSpentLiving']
        if 'maxTotalPlayerScore' in kwargs:
            self.max_total_player_score = kwargs['maxTotalPlayerScore']
        if 'mostChampionKillsPerSession' in kwargs:
            self.most_champion_kills_per_session = kwargs['mostChampionKillsPerSession']
        if 'mostSpellsCast' in kwargs:
            self.most_spells_cast = kwargs['mostSpellsCast']
        if 'normalGamesPlayed' in kwargs:
            self.normal_games_played = kwargs['normalGamesPlayed']
        if 'rankedPremadeGamesPlayed' in kwargs:
            self.ranked_premade_games_played = kwargs['rankedPremadeGamesPlayed']
        if 'rankedSoloGamesPlayed' in kwargs:
            self.ranked_solo_games_played = kwargs['rankedSoloGamesPlayed']
        if 'totalAssists' in kwargs:
            self.total_assists = kwargs['totalAssists']
        if 'totalChampionKills' in kwargs:
            self.total_champion_kills = kwargs['totalChampionKills']
        if 'totalDamageDealt' in kwargs:
            self.total_damage_dealt = kwargs['totalDamageDealt']
        if 'totalDamageTaken' in kwargs:
            self.total_damage_taken = kwargs['totalDamageTaken']
        if 'totalDoubleKills' in kwargs:
            self.total_double_kills = kwargs['totalDoubleKills']
        if 'totalFirstBlood' in kwargs:
            self.total_first_blood = kwargs['totalFirstBlood']
        if 'totalGoldEarned' in kwargs:
            self.total_gold_earned = kwargs['totalGoldEarned']
        if 'totalHeal' in kwargs:
            self.total_heal = kwargs['totalHeal']
        if 'totalMagicDamageDealt' in kwargs:
            self.total_magic_damage_dealt = kwargs['totalMagicDamageDealt']
        if 'totalMinionKills' in kwargs:
            self.total_minion_kills = kwargs['totalMinionKills']
        if 'totalNeutralMinionsKilled' in kwargs:
            self.total_neutral_minions_killed = kwargs['totalNeutralMinionsKilled']
        if 'totalNodeCapture' in kwargs:
            self.total_node_capture = kwargs['totalNodeCapture']
        if 'totalNodeNeutralize' in kwargs:
            self.total_node_neutralize = kwargs['totalNodeNeutralize']
        if 'totalPentaKills' in kwargs:
            self.total_penta_kills = kwargs['totalPentaKills']
        if 'totalPhysicalDamageDealt' in kwargs:
            self.total_physical_damage_dealt = kwargs['totalPhysicalDamageDealt']
        if 'totalQuadraKills' in kwargs:
            self.total_quadra_kills = kwargs['totalQuadraKills']
        if 'totalSessionsLost' in kwargs:
            self.total_sessions_lost = kwargs['totalSessionsLost']
        if 'totalSessionsPlayed' in kwargs:
            self.total_sessions_played = kwargs['totalSessionsPlayed']
        if 'totalSessionsWon' in kwargs:
            self.total_sessions_won = kwargs['totalSessionsWon']
        if 'totalTripleKills' in kwargs:
            self.total_triple_kills = kwargs['totalTripleKills']
        if 'totalTurretsKilled' in kwargs:
            self.total_turrets_killed = kwargs['totalTurretsKilled']
        if 'totalUnrealKills' in kwargs:
            self.total_unreal_kills = kwargs['totalUnrealKills']

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


class MasteryPage(object):
    """
    current     boolean             Indicates if the mastery page is the current mastery page.
    id          long                Mastery page ID.
    name        string              Mastery page name.
    talents     List[TalentDto]     List of mastery page talents associated with the mastery page.
    """
    def __init__(self, **kwargs):
        self.current = kwargs['current']
        self.id = kwargs['id']
        self.name = kwargs['name']

        if 'talents' in kwargs:
            talents = []
            for talent in kwargs['talents']:
                talents.append(Talent(**talent))
            self.talents = talents

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


class Talent(object):
    """
    id      int         Talent id.
    name    string      Talent name.
    rank    int         Talent rank.
    """
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.rank = kwargs['rank']

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


class RunePage(object):
    """
    current     boolean             Indicates if the page is the current page.
    id          long                Rune page ID.
    name        string              Rune page name.
    slots       List[RuneSlotDto]   List of rune slots associated with the rune page.
    """
    def __init__(self, **kwargs):
        self.current = kwargs['current']
        self.id = kwargs['id']
        self.name = kwargs['name']

        if 'slots' in kwargs:
            slots = []
            for slot in kwargs['slots']:
                slots.append(RuneSlot(**slot))
            self.slots = slots

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


class RuneSlot(object):
    """
    rune            RuneDto     Rune associated with the rune slot.
    runeSlotId      int         Rune slot ID.
    """
    def __init__(self, **kwargs):
        self.rune_id = kwargs['runeId']
        self.slot_id = kwargs['runeSlotId']

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


class Rune(object):
    """
    description     string      Rune description.
    id              int         Rune ID.
    name            string      Rune name.
    tier            int         Rune tier.
    """
    def __init__(self, **kwargs):
        self.description = kwargs['description']
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.tier = kwargs['tier']

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


class Team(object):
    """
    createDate                      Date    
    fullId                          string  
    lastGameDate                    Date    
    lastJoinDate                    Date    
    lastJoinedRankedTeamQueueDate   Date    
    matchHistory                    List[MatchHistorySummaryDto]    
    messageOfDay                    MessageOfDayDto 
    modifyDate                      Date    
    name                            string  
    roster                          RosterDto   
    secondLastJoinDate              Date    
    status                          string  
    tag                             string  
    teamStatSummary                 TeamStatSummaryDto  
    thirdLastJoinDate               Date
    """
    def __init__(self, **kwargs):
        self.create_date = utils.convert_epoch_millis_to_datetime(kwargs['createDate'])
        self.full_id = kwargs['fullId']
        self.last_game_date = utils.convert_epoch_millis_to_datetime(kwargs['lastGameDate'])
        self.last_join_date = utils.convert_epoch_millis_to_datetime(kwargs['lastJoinDate'])
        self.last_joined_ranked_team_queue_date = utils.convert_epoch_millis_to_datetime(kwargs['lastJoinedRankedTeamQueueDate'])
        
        match_history = []
        for match in kwargs['matchHistory']:
            match_history.append(MatchHistorySummary(**match))
        self.match_history = match_history
        self.modify_date = utils.convert_epoch_millis_to_datetime(kwargs['modifyDate'])
        self.name = kwargs['name']
        self.roster = Roster(**kwargs['roster'])
        self.second_last_join_date = utils.convert_epoch_millis_to_datetime(kwargs['secondLastJoinDate'])
        self.status = kwargs['status']
        self.tag = kwargs['tag']

        team_stat_details = []
        for stat_detail in kwargs['teamStatDetails']:
            team_stat_details.append(TeamStatDetail(**stat_detail))
        self.team_stat_details = team_stat_details

        self.third_last_join_date = utils.convert_epoch_millis_to_datetime(kwargs['thirdLastJoinDate'])

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


class MatchHistorySummary(object):
    """
    assists             int 
    deaths              int 
    gameId              long    
    gameMode            string  
    invalid             boolean 
    kills               int 
    mapId               int 
    opposingTeamKills   int 
    opposingTeamName    string  
    win                 boolean
    """
    def __init__(self, **kwargs):
        self.assists = kwargs['assists']
        self.deaths = kwargs['deaths']
        self.game_id = kwargs['gameId']
        self.game_mode = kwargs['gameMode']
        self.invalid = kwargs['invalid']
        self.kills = kwargs['kills']
        self.map_id = kwargs['mapId']
        self.opposing_team_kills = kwargs['opposingTeamKills']
        self.opposing_team_name = kwargs['opposingTeamName']
        self.win = kwargs['win']

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


class MessageOfDay(object):
    """
    createDate      long    
    message         string  
    version         int
    """
    def __init__(self, **kwargs):
        self.create_date = utils.convert_epoch_millis_to_datetime(kwargs['createDate'])
        self.message = kwargs['message']
        self.version = kwargs['version']

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


class Roster(object):
    """
    memberList      List[TeamMemberInfoDto] 
    ownerId         long
    """
    def __init__(self, **kwargs):
        member_list = []
        for member in kwargs['memberList']:
            member_list.append(TeamMemberInfo(**member))
        self.member_list = member_list

        self.owner_id = kwargs['ownerId']

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


class TeamStatDetail(object):
    """
    averageGamesPlayed  int
    losses              int
    teamStatType        string
    wins                int
    """
    def __init__(self, **kwargs):
        self.average_games_played = kwargs['averageGamesPlayed']
        self.losses = kwargs['losses']
        self.team_stat_type = kwargs['teamStatType']
        self.wins = kwargs['wins']


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


class TeamMemberInfo(object):
    """
    inviteDate      Date    
    joinDate        Date    
    playerId        long    
    status          string
    """
    def __init__(self, **kwargs):
        self.invite_date = utils.convert_epoch_millis_to_datetime(kwargs['inviteDate'])
        self.join_date = utils.convert_epoch_millis_to_datetime(kwargs['joinDate'])
        self.player_id = kwargs['playerId']
        self.status = kwargs['status']

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


class Static(object):
    """
    Holds data return from pyriot.static_champions()

    data	Map[string, ChampionDto]
    format	string
    keys	Map[string, string]
    type	string
    version	string

    ChampionDto => class StaticChampion
    """
    def __init__(self, **kwargs):

        data = {}
        for key, value in kwargs['data'].iteritems():
            data[key] = StaticChampion(**value)
        self.data = data

        self.format = kwargs['format']

        keys = {}
        for key, value in kwargs['keys'].iteritems():
            data[key] = value
        self.keys = keys

        self.type = kwargs['type']
        self.version = kwargs['version']

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


class StaticChampion(object):
    """
    allytips	List[string]
    blurb	    string
    enemytips	List[string]
    id	        int
    image	    ImageDto
    info    	InfoDto
    key	        string
    lore	    string
    name	    string
    partype	    string
    passive	    PassiveDto
    recommended	List[RecommendedDto]
    skins	    List[SkinDto]
    spells	    List[ChampionSpellDto]
    stats   	StatsDto
    tags	    List[string]
    title   	string

    ImageDto         => class Image
    InfoDto          => class Info
    PassiveDto       => class Passive
    RecommendedDto   => class Recommended
    SkinDto          => class Skin
    ChampionSpellDto => class Spell
    StatsDto         => class Stats
    """

    def __init__(self, **kwargs):
        ally_tips = []
        #for ally_tip in kwargs['allytips']:
            # ally_tips.append(ally_tip)
        # self.ally_tips = ally_tips

        # self.blurb = kwargs['blurb']

        # enemy_tips = []
        # for enemy_tip in kwargs['enemytips']:
        #     enemy_tips.append(enemy_tip)
        # self.enemy_tips = enemy_tips

        self.id = kwargs['id']
        # self.image = Image(**kwargs['image'])
        # self.info = Info(**kwargs['info'])
        self.key = kwargs['key']
        # self.lore = kwargs['lore']
        self.name = kwargs['name']
        # self.partype = kwargs['partype']
        # self.passive = Passive(**kwargs['passive'])

        # recommended = []
        # for rec in kwargs['recommended']:
        #     recommended.append(Recommended(**rec))
        # self.recommended = recommended

        # skins = []
        # for skin in kwargs['skins']:
        #     skins.append(Skin(**skin))
        # self.skins = skins

        # spells = []
        # for spell in kwargs['spell']:
        #     spells.append(Spell(**spell))
        # self.spells = spells

        # self.stats = Stats(**kwargs['stats'])

        # tags = []
        # for tag in kwargs['tags']:
        #     tags.append(kwargs['tags'])
        # self.tags = tags

        self.title = kwargs['title']

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


class Image(object):
    """
    full	string
    group	string
    h	    int
    sprite	string
    w	    int
    x	    int
    y	    int
    """
    def __init__(self, **kwargs):
        self.full = kwargs['full']
        self.group = kwargs['group']
        self.h = kwargs['h']
        self.sprite = kwargs['sprite']
        self.v = kwargs['v']
        self.x = kwargs['x']
        self.y = kwargs['y']

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


class Info(object):
    """
    attack	    int
    defense	    int
    difficulty	int
    magic	    int
    """
    def __init__(self, **kwargs):
        self.attack = kwargs['attack']
        self.defense = kwargs['defense']
        self.difficulty = kwargs['difficulty']
        self.magic = kwargs['magic']

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


class Passive(object):
    """
    description	            string
    image	                ImageDto
    name	                string
    sanitizedDescription	string

    ImageDto => class Image
    """

    def __init__(self, **kwargs):
        self.description = kwargs['description']
        self.image = Image(**kwargs['image'])
        self.name = kwargs['name']
        self.sanitized_description = kwargs['sanitizedDescription']

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


class Recommended(object):
    """
    blocks	    List[BlockDto]
    champion	string
    map	        string
    mode	    string
    priority	boolean
    title   	string
    type	    string

    BlockDto => class Block
    """

    def __init__(self, **kwargs):
        blocks = []
        for block in kwargs['blocks']:
            blocks.append(Block(**block))
        self.blocks = blocks

        self.champion = kwargs['champion']
        self.map = kwargs['map']
        self.mode = kwargs['mode']
        self.priority = kwargs['priority']
        self.title = kwargs['title']
        self.type = kwargs['type']

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


class Spell(object):
    """
    *** NOT DONE WITH INIT ***

    ChampionSpellDto
    altimages       List[ImageDto]
    cooldown        List[double]
    cooldownBurn    string
    cost            List[int]
    costBurn        string
    costType        string
    description     string
    effect          List[object]	This field is a List of List of Integer.
    effectBurn      List[string]
    image           ImageDto
    key	            string
    leveltip	    LevelTipDto
    maxrank	        int
    name	        string
    range	        object	This field is either a List of Integer or the String 'self' for spells that target one's own champion.
    rangeBurn	    string
    resource	    string
    sanitizedDescription	string
    sanitizedTooltip	    string
    tooltip	        string
    vars	        List[SpellVarsDto]

    ImageDto     => class Image
    LevelTipDto  => class LevelTip
    SpellVarsDto => class SpellVars
    """
    def __init__(self, **kwargs):
        self.image = Image(**kwargs['image'])
        self.key = kwargs['key']
        self.tooltip = kwargs['tooltip']

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


class Skin(object):
    """
    id	    int
    name	string
    num	    int
    """

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.num = kwargs['num']

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


class Stats(object):
    """
    armor	                double
    armorperlevel	        double
    attackdamage	        double
    attackdamageperlevel	double
    attackrange	            double
    attackspeedoffset	    double
    attackspeedperlevel	    double
    crit	                double
    critperlevel	        double
    hp	                    double
    hpperlevel	            double
    hpregen	                double
    hpregenperlevel	        double
    movespeed	            double
    mp	                    double
    mpperlevel	            double
    mpregen	                double
    mpregenperlevel	        double
    spellblock	            double
    spellblockperlevel	    double
    """

    def __init__(self, **kwargs):
        self.armor = kwargs['armor']
        self.armor_per_level = kwargs['armorperlevel']
        self.attack_damage = kwargs['attackdamage']
        self.attack_damage_per_level = kwargs['attackdamageperlevel']
        self.attack_range = kwargs['attackrange']
        self.attack_speed_offset = kwargs['attackspeedoffset']
        self.attack_speed_per_level = kwargs['attackspeedperlevel']
        self.crit = kwargs['crit']
        self.crit_per_level = kwargs['critperlevel']
        self.hp = kwargs['hp']
        self.hp_per_level = kwargs['hpperlevel']
        self.hp_regen = kwargs['hpregen']
        self.hp_regen_per_level = kwargs['hpregenperlevel']
        self.move_speed = kwargs['movespeed']
        self.mp = kwargs['mp']
        self.mp_per_level = kwargs['mpperlevel']
        self.mp_regen = kwargs['mpregen']
        self.mp_regen_per_level = kwargs['mpregenperlevel']
        self.spell_block = kwargs['spellblock']
        self.spell_block_per_level = kwargs['spellblockperlevel']

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


class Block(object):
    """
    items	List[BlockItemDto]
    recMath	boolean
    type	string

    BlockItemDto => class BlockItem
    """
    def __init__(self, **kwargs):
        items = []
        for item in kwargs['items']:
            items.append(BlockItem(**item))
        self.items = items

        self.rec_math = kwargs['recMath']
        self.type = kwargs['type']

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


class BlockItem(object):
    """
    count	int
    id	    int
    """
    def __init__(self, **kwargs):
        self.count = kwargs['count']
        self.id = kwargs['id']

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
