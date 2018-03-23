import re

arq = open('qgame.txt', 'r')
text = arq.readlines()
players_1ist, killers_list, world_list = [], [], []
dict_killer = {}
kills = 0
i = 0
players = ''
means_of_death = {'MOD_UNKNOWN': 0, 'MOD_SHOTGUN': 0, 'MOD_GAUNTLET': 0, 'MOD_MACHINEGUN': 0, 'MOD_GRENADE': 0,
                  'MOD_GRENADE_SPLASH': 0, 'MOD_ROCKET': 0, 'MOD_ROCKET_SPLASH': 0, 'MOD_PLASMA': 0,
                  'MOD_PLASMA_SPLASH': 0,
                  'MOD_RAILGUN': 0, 'MOD_LIGHTNING': 0, 'MOD_BFG': 0, 'MOD_BFG_SPLASH': 0, 'MOD_WATER': 0,
                  'MOD_SLIME': 0,
                  'MOD_LAVA': 0, 'MOD_CRUSH': 0, 'MOD_TELEFRAG': 0, 'MOD_FALLING': 0, 'MOD_SUICIDE': 0,
                  'MOD_TARGET_LASER': 0,
                  'MOD_TRIGGER_HURT': 0, 'MOD_NAIL': 0, 'MOD_CHAINGUN': 0, 'MOD_PROXIMITY_MINE': 0, 'MOD_KAMIKAZE': 0,
                  'MOD_JUICED': 0, 'MOD_GRAPPLE': 0}

for line in text:
    # busca dos jogadores
    player = re.search(r'(n\\.*?\\t)', line)
    # busca das mortes
    matou = re.search(r'(killed)', line)
    new_game = re.search(r'(ShutdownGame:)', line)
    if player:
        player = re.sub(r'(n\\)', "", player.group(0))
        player = re.sub(r'\\t', "", player)
        players_1ist.append(player)
    if matou:
        kills += 1
        players = set(players_1ist)
        mean = re.search(r'(by.*$)', line)
        mean = re.sub(r'by', "", mean.group(0))
        mean = re.sub(r' ', "", mean)
        means_of_death[mean] += 1
        # Criando  dicionario para incluir o número de kills dos jogadores

        for killer in players:
            dict_killer[killer] = 0
        for j in players:
            str = j + ' killed'
            world_kills = '<world> killed ' + j
            if line.find(str) != -1:
                killers_list.append(j)
            if line.find(world_kills) != -1:
                world_list.append(j)
        for mat in killers_list:
            dict_killer[mat] += 1
        for morreu in world_list:
            dict_killer[morreu] -= 1
    if new_game:
        i += 1
        print('-' * 180)
        print('game ', i, '\nJogadores: ', players, '\nTotal de Mortes:', kills, '\nMortes:', dict_killer,
              '\nClassificação:')
        classificacao = sorted(dict_killer, key=dict_killer.get, reverse=True)

        for ordem in classificacao:
            print(ordem, dict_killer[ordem])
        print('Causa da Morte: ', means_of_death)

        # Zerando as variáveis

        for m in means_of_death:
            means_of_death[m] = 0
        players_1ist, killers_list, world_list = [], [], []
        players = ''
        dict_killer = {}
        kills = 0
arq.close()
