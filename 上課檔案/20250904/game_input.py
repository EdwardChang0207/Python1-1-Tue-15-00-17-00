def game_input(game_map, player):
    while True:
        x, y = [int(i) for i in input().split()]
        if not game_map[x][y]:
            game_map[x][y] = player
            return game_map
        else:
            print('Error')