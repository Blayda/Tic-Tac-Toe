from helpers import draw_board, check_turn, check_for_wins
import os
#Dictionary
spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
          6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    #Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    #If prev spot selecter inform player that spot is taken
    if prev_turn == turn:
        print("Invalid spot selected, please select another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit")
    #Player input
    choice = input()
    if choice == 'q':
        playing = False
    #Check if player gave number 1-9
    elif str.isdigit(choice) and int(choice) in spots:
    #Check if the spot has already been taken
        if not spots[int(choice)] in {"X", "O"}:
            # Valid unput, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)
    if check_for_wins(spots): playing, complete = False, True
    if turn > 8: playing = False

#Out of the loop present the results
#Draw the board one last time
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
#if there was a winner, say who won
if complete:
    if check_turn(turn) == 'X': print("Player 1 Wins!🤩")
    else: print("Player 2 Wins!🤩")
else:
    #Tie game
    print("No Winner🥲")

print("Thanks for playing!❤️")


