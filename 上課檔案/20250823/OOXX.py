game_map = [
    ['','',''],
    ['','',''],
    ['','','']
]

# game_map = [['','',''],['','',''],['','','']]

#1 1, 0 0
player = 'O'
game = True
while game:
    print(f'It\'s {player}\'s Turn!')
    x, y = [int(i) for i in input().split()] #'1 1'- > ['1','1']
    if game_map[x][y]: 
        print('ERROR pls enter again!')
        continue
    game_map[x][y] = player
    print(*game_map,sep='\n')
    
    space = 0
    for i in range(len(game_map)):
        if game_map[i].count(player) == 3:
            print(f'{player} Win!')
            game = False
            break
        col = [game_map[0][i],game_map[1][i],game_map[2][i]]
        if col.count(player) == 3:
            print(f'{player} Win!')
            game = False
            break
        if [game_map[0][0],game_map[1][1],game_map[2][2]].count(player) == 3:
            print(f'{player} Win!')
            game = False
            break
        if [game_map[0][2],game_map[1][1],game_map[2][0]].count(player) == 3:
            print(f'{player} Win!')
            game = False
            break
        space += game_map[i].count('')

    if space == 0:
        print(f'Tie!')
        game = False
        

    if player == 'O': player = 'X'
    else: player = 'O'


