from game_init import game_init
from game_input import game_input
game_map, player, game = game_init()
while game:
    print(f'It\'s {player}\'s Turn!')
    game_map = game_input(game_map, player)
    print(*game_map, sep='\n')