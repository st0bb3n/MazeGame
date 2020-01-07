from sys import exit

board = [
        ['x ',' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',' 8 ',' 9 ',' 10',' 11',' 12',' 13',' 14',' 15',' x',' x'],
        ['--','---','---','---','---','---','---','---','---','---','---','---','---','---','---','---','--',' x'], #generates board
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |',' 2'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |',' 3'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |',' 4'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |',' 5'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |',' 6'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |',' 7'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' O ',' O ',' O ',' @ ',' . ',' . ',' . ',' . ',' . ',' . ',' |',' 8'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' @ ',' . ',' . ',' @ ',' . ',' . ',' . ',' . ',' . ',' . ',' |',' 9'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' @ ',' . ',' . ',' @ ',' . ',' . ',' . ',' . ',' . ',' . ',' |','10'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' @ ',' @ ',' @ ',' @ ',' . ',' . ',' . ',' . ',' . ',' . ',' |','11'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |','12'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' @ ',' @ ',' @ ',' . ',' |','13'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' O ',' F ',' @ ',' . ',' |','14'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' O ',' @ ',' @ ',' . ',' |','15'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |','16'],
        ['| ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' . ',' |','17'],
        ['--','---','---','---','---','---','---','---','---','---','---','---','---','---','---','---','--',' x']
        ]

#todo map
def showGrid(): #shows the grid
    for i in range(0,19):
        #print(grid[i])
        row = ''.join(map(str, board[i]))
        print(row)

posY = 10  #start pos
posX = 8
turns = 0
smashes = 0

#todo diagonal movement + movement power

def move_up():
    global posX
    global posY
    board[posY][posX] = ' . '
    posY -= 1
    board[posY][posX] = ' S '
    showGrid()
    print(posX,posY)

def move_down():
    global posX
    global posY
    board[posY][posX] = ' . '
    posY += 1
    board[posY][posX] = ' S '
    showGrid()
    print(posX,posY)

def move_left():
    global posX
    global posY
    board[posY][posX] = ' . '
    posX -= 1
    board[posY][posX] = ' S '
    showGrid()
    print(posX,posY)

def move_right():
    global posX
    global posY
    board[posY][posX] = ' . '
    posX += 1
    board[posY][posX] = ' S '
    showGrid()
    print('Current position:', posX, posY)

def smash():
    global posX
    global posY
    if (board[posY - 1][posX] != ' @ ') and (board[posY - 1][posX] == ' . ' or ' O '):
        board[posY - 1][posX] = ' . '
    if (board[posY + 1][posX] != ' @ ') and (board[posY + 1][posX] == ' . ' or ' O '):
        board[posY + 1][posX] = ' . '
    if (board[posY][posX - 1] != ' @ ') and (board[posY][posX - 1] == ' . ' or ' O '):
        board[posY][posX - 1] = ' . '
    if (board[posY][posX + 1] != ' @ ') and (board[posY][posX + 1] == ' . ' or ' O '):
        board[posY][posX + 1] = ' . '
    if (board[posY - 1][posX - 1] != ' @ ') and (board[posY - 1][posX - 1] == ' . ' or ' O '):
        board[posY - 1][posX - 1] = ' . '
    if (board[posY + 1][posX + 1] != ' @ ') and (board[posY - 1][posX - 1] == ' . ' or ' O '):
        board[posY + 1][posX + 1] = ' . '
    if (board[posY - 1][posX + 1] != ' @ ') and (board[posY - 1][posX - 1] == ' . ' or ' O '):
        board[posY - 1][posX + 1] = ' . '
    if (board[posY + 1][posX - 1] != ' @ ' ) and (board[posY - 1][posX - 1] == ' . ' or ' O '):
        board[posY + 1][posX - 1] = ' . '
    showGrid()

def win():
    print('You WIN!')
    print('You took', turns, 'turns')
    print('You used', smashes, 'smashes')
    exit()
board[posY][posX] = ' S '
showGrid()

print('Get the F')
try:
    while True: #todo end movement
        m = int(input('Movement: '))
        if m == 8 and board[posY - 1][posX] == ' . ' :
            move_up()
            turns += 1
        if m == 2 and board[posY + 1][posX] == ' . ':
            move_down()
            turns += 1
        if m == 4 and board[posY][posX - 1] == ' . ':
            move_left()
            turns += 1
        if m == 6 and board[posY][posX + 1] == ' . ':
            move_right()
            turns += 1
        if m == 8 and board[posY - 1][posX] == ' F ' :
            move_up()
            turns += 1
            win()
        if m == 2 and board[posY + 1][posX] == ' F ':
            move_down()
            turns += 1
            win()
        if m == 4 and board[posY][posX - 1] == ' F ':
            move_left()
            turns += 1
            win()
        if m == 6 and board[posY][posX + 1] == ' F ':
            move_right()
            turns += 1
            win()
        if m == 5:
            smash()
            print('!SMASH!')
            smashes += 1
        if m != (2 or 4 or 6 or 8 or 5):
            pass
except:
    pass

'''
if __name__ == '__main__':
  main()
'''
