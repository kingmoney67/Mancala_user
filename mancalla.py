

BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board should be called in order to draw the board.
    """

    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline                                                                                                                                                                                          
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """                                                                                                                                                                                                     
        Draw_mancala is a helper function for the draw_board function.                                                                                                                                      
    :param fore_or_aft: front or back (0, or 1)                                                                                                                                                             
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH                                                                                                 
    2d-list of characters which we are creating to print the board.                                                                                                                     
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
      for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


# Gets the player name                                                                                                                                                                                      
def get_player(mancala_a, mancala_b):
    # ask player one for there name                                                                                                                                                                         
    player_1 = input('Player 1 please tell me your name: ')
    for x in range(len(mancala_a)):
        # switch from Boris to whatever the user enters                                                                                                                                                     
        if mancala_a[x] == 'Boris  ':
            mancala_a[x] = player_1
    # ask player two for name                                                                                                                                                                               
    player_2 = input('Player 2 please tell me your name: ')
    for x in range(len(mancala_b)):
        if mancala_b[x] == 'Abby   ':
            mancala_b[x] = player_2
    # return players in a list                                                                                                                                                                              
    return [player_1, player_2]


def take_turn(player1, player2, count_turn, top_cups, bottom_cups, mancala_a, mancala_b):
    # list with all the numbers that are on the board to make sure other values are not entered                                                                                                             
    strin_valid = ['1', '2', '3', '4', '5', '6', '8', '9', '10', '11', '12', '13']
    # if the count is even first player goes                                                                                                                                                                
    if count_turn % 2 == 0:
        print(player1, end='')
        # create variable saving what user inputs                                                                                                                                                           
        move = input(' What cup do you want to move? ')
        # for loop going through the first 2d list to check if what move the player selected is not already 0                                                                                               
        for x in range(len(top_cups)):
            for i in range(len(top_cups[x])-2):
                if top_cups[x][i] == move:
                    check = top_cups[x][i+2]
                    if check == '0':
                        print('Theres no stone in that cup')
                        print('Go again...')
                        # return one so it can be subtracted from the count variable making the player go again                                                                                             
                        return -1
        # for loop going through the second 2d list to check if what move the player selected is not already 0                                                                                              
        for x in range(len(bottom_cups)):
            for i in range(len(bottom_cups[x])-2):
                if bottom_cups[x][i] == move:
                    if bottom_cups[x][i+2] == '0':
                        print('Theres no stone in that cup')
                        print('Go again...')
                        # return one so it can be subtracted from the count variable making the player go again                                                                                             
                        return -1

        # if the player types in something that is not in the valid list of arguments accepted then it would ask them to enter again                                                                        
        while move not in strin_valid:
            print('Pick a number on the Board')
            print(player1, end='')
            move = input(' What cup do you want to move? ')
        # int move before returning it since you have to do calculation with it in run game                                                                                                                 
        move = int(move)

    # if the count is odd then the second player goes                                                                                                                                                       
    # copy pasted the arguments that were above below but for the second player                                                                                                                             
    elif count_turn % 2 != 0:
        print(player2, end='')
        move = input(' What cup do you want to move? ')

        for x in range(len(top_cups)):
            for i in range(len(top_cups[x])-2):
                if top_cups[x][i] == move:
                    check = top_cups[x][i + 2]
                    if check == '0':
                        print('Theres no stone in that cup')
                        print('Go again...')

                        return -1
        for x in range(len(bottom_cups)):
            for i in range(len(bottom_cups[x])-2):
                if bottom_cups[x][i] == move:
                    check = bottom_cups[x][i+2]
                    if check == '0':
                        print('Theres no stone in that cup')
                        print('Go again...')

                        return -1
        # if the player types in something that is not in the valid list of arguments accepted then it would ask them to enter again                                                                        
        while move not in strin_valid:
            print('Pick a number on the Board')
            print(player2, end='')
            move = input(' What cup do you want to move? ')
        move = int(move)

    return move

# Finds out who the winner is by running and checking till one side of the board has zero stones                                                                                                            
def win_game(first_2d, second_2d, mancala_a, mancala_b,player):
    # make a bool variable if bool is true keep on running                                                                                                                                                  
    bool = True
    # count variable to check the 0's in a list                                                                                                                                                             
    count = 0
    # for loop running through the first 2d list                                                                                                                                                            
    for x in range(len(first_2d)):
        # check if the stones are zero throughout                                                                                                                                                           
        if (int(first_2d[x][3])) == 0:
            # if zero add 1 to count                                                                                                                                                                        
            count += 1
            # if count 6 that means that list is all 0's                                                                                                                                                    
            if count == 6:
                # count false would stop while loop                                                                                                                                                         
                bool = False
                # check which mancala has more stones                                                                                                                                                       
                if (int(mancala_a[8])) > (int(mancala_b[8])):
                    draw_board(first_2d, second_2d, mancala_a, mancala_b)
                    print(player[0],'is the winner')
                    # return bool inside so it doesnt go to the else statement and becomes true                                                                                                             
                    return bool
                else:
                    draw_board(first_2d, second_2d, mancala_a, mancala_b)
                    print(player[1],'is the winner')
                    return bool
        else:
            bool = True
    count = 0
    # same for loop but for the second 2d list                                                                                                                                                              
    # for loop running through the second 2d list                                                                                                                                                           
    for x in range(len(second_2d)):
        if (int(second_2d[x][3])) == 0:
            count += 1
            if count == 6:
                bool = False

                if (int(mancala_a[8])) > (int(mancala_b[8])):
                    draw_board(first_2d, second_2d, mancala_a, mancala_b)
                    print(player[0],'is the winner')
                    return bool
                else:
                    draw_board(first_2d, second_2d, mancala_a, mancala_b)
                    print(player[1],'is the winner')
                    return bool

        else:
            bool = True

    return bool

# responsible for changing the actual 2d board at the end of the run game program after the move_stones list has been changed                                                                               
def change_board(move_stones,top_cups,bottom_cups,mancala_a,mancala_b):
    # for loop running from 0,14 since that are all the possible entries in the game                                                                                                                        
    for x in range(0, 14):
        # if x=0 it is the first mancala                                                                                                                                                                    
        if x == 0:
            # change the mancala board at the given spot, which is mancala_a 8 in this scenario                                                                                                             
            manc = int(mancala_a[8]) + move_stones[x]
            # add space after the number since the list requires space to form the board                                                                                                                    
            manca = str(manc) + '     '
            mancala_a[8] = manca
        # makes changes in the top cups list                                                                                                                                                                
        if x <= 6 and x >= 1:
            # changes top cups to what move stones where changed to                                                                                                                                         
            up_cup = int(top_cups[x - 1][3]) + move_stones[x]
            top_cups[x - 1][3] = str(up_cup)
        # x=7 is our second mancala whiich in mancala_b would be at index 8                                                                                                                                 
        if x == 7:
            manc = int(mancala_b[8]) + move_stones[x]
            # add space at the end since the list requires space to form the board                                                                                                                          
            manca = str(manc) + '     '
            mancala_b[8] = manca
        # makes changes to the second 2d list                                                                                                                                                               
        elif x >= 8 and x <= 13:
            # changes bottom cups to what the stone cups where changed too                                                                                                                                  
            down_cup = int(bottom_cups[7 - x][3]) + move_stones[x]
            bottom_cups[7 - x][3] = str(down_cup)


def run_game():
    # first 2d list used for the top cups                                                                                                                                                                   
    top_cups = [['Cup   ', '1', 'Stones', '4', '      '],
                ['Cup   ', '2', 'Stones', '4', '      '],
                ['Cup   ', '3', 'Stones', '4', '      '],
                ['Cup   ', '4', 'Stones', '4', '      '],
                ['Cup   ', '5', 'Stones', '4', '      '],
                ['Cup   ', '6', 'Stones', '4', '      ']]
    # second 2d list used for the bottom list                                                                                                                                                               
    bottom_cups = [['Cup   ', '13', 'Stones', '4', '      '],
                   ['Cup   ', '12', 'Stones', '4', '      '],
                   ['Cup   ', '11', 'Stones', '4', '      '],
                   ['Cup   ', '10', 'Stones', '4', '      '],
                   ['Cup   ', '9', 'Stones', '4', '      '],
                   ['Cup   ', '8', 'Stones', '4', '      ']]
    # list forming the first mancala                                                                                                                                                                        
    mancala_a = ['      ', '      ', '      ', 'Boris  ', '      ', '      ', '      ', 'Stones',
                 '0     ', '      ', '      ']
    # list forming the second mancala                                                                                                                                                                       
    mancala_b = ['      ', '      ', '      ', 'Abby   ', '      ', '      ', '      ', 'Stones',
                 '0     ', '      ', '      ']
    # replacement for the stones value in both the first and the second 2d list                                                                                                                             
    move_stones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # calls the get player fucntion to get the players name                                                                                                                                                 
    player = get_player(mancala_a, mancala_b)
    # starting count 2 so it is even and player1 can go first                                                                                                                                               
    turn_count = 2
    # runs the win game function till false                                                                                                                                                                 
    # win game checks to see when one of the 2d list will have all stones as zero                                                                                                                           
    while win_game(top_cups, bottom_cups, mancala_a, mancala_b,player):
        # count value to change whatever move someone picks to 0                                                                                                                                            
        stones = 0
        # Draws board by taking in both the 2d list and the two mancala lists                                                                                                                               
        draw_board(top_cups, bottom_cups, mancala_a, mancala_b)
        # variable keeping track of the player moves                                                                                                                                                        
        move = take_turn(player[0], player[1], turn_count, top_cups, bottom_cups, mancala_a, mancala_b)
        # move outputs -1 if the player picks a cup that is already 0                                                                                                                                       
        if move == -1:
            turn_count -= 1
        # count +=1 after a players turn                                                                                                                                                                    
        turn_count += 1
        # Goes through the range of the top list                                                                                                                                                            
        if move <= 6 and move >= 1:
            for g in top_cups:
                for e in g[3]:
                    if g[1] == str(move):
                        stones = int(e)
        # Goes through the range of the bottom list                                                                                                                                                         
        elif move >= 7 and move <= 13:
            for x in bottom_cups:
                for e in x[3]:
                    if x[1] == str(move):
                        stones = int(e)
        # makes sure mancala doesnt go out of range                                                                                                                                                         
        og_mancala = (stones + move) % 7
        # print out that you landed on a mancala                                                                                                                                                            
        if og_mancala == 0:
            print('Your last stone landed in a mancala.')
            print('Go again...')
            # subtract one from turn count so the player can go again                                                                                                                                       
            turn_count -= 1
        # goes in the move stone list where the person move is                                                                                                                                              
        move_stones[move] = 0
        # changes all the 0's after and adds one =                                                                                                                                                          
        # changes all the 0's after and adds one =                                                                                                                                                          
        count = move + 1
        while stones > 0:
            # resets when count is 0                                                                                                                                                                        
            if count == 14:
                count = 0
            move_stones[count] += 1
            stones -= 1
            count += 1
        # Changes the move that the person picked to 0 in the first list                                                                                                                                    
        if move <= 6 and move >= 1:
            for g in top_cups:
                for e in g[3]:
                    if g[1] == str(move):
                        g[3] = '0'

        # Changes the move that the person picked to 0 in the second                                                                                                                                        
        elif move >= 7 and move <= 13:
            for x in bottom_cups:
                for e in x[3]:
                    if x[1] == str(move):
                        x[3] = '0'
        # uses the chnaged move_stones list to make actual changes to the 2d list so it can be printed using draw board                                                                                     
        change_board(move_stones,top_cups,bottom_cups,mancala_a,mancala_b)

        # resets the whole love stones list after the change has been made                                                                                                                                  
        move_stones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    pass

if __name__ == "__main__":
  # call function to run the whole game                                                                                                                                                                  
  run_game()

