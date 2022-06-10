from modules.Player import Player
from modules.Board import Board

# set up initial variables and start while loop to make replayable
playing = True
print("\n\tWelcome to Tic Tac Toe!")
p1 = Player(1)
p2 = Player(2)
    
while playing:
    # set grid to be full of blank spaces
    board = Board([" "]*9)
    # set turn count to 0 
    t_count = 0
    # player 1 chooses symbol, allocate other to player 2
    p1.set_symbol()
    if p1.symbol == "x":
        p2.symbol = "o"
    else:
        p2.symbol = "x"
    # set player with "x" to go first
    if p1.symbol == "x":
        f_player = p1
        s_player = p2
    else:
        f_player = p2
        s_player = p1
    # the main game
    board.play()
    run = 1         # main play loop for each turn
    while run:
        t_count +=1         # up the turn counter to check whose go it is
        if t_count%2 == 1:
            c_player = f_player
        else:
            c_player = s_player
        run2 = 1
        while run2:         # current player picks a square to play their symbol and make sure it's an empty square
            run3 = 1
            while run3:
                square = (int(input(f"{c_player.name}'s turn. Pick a square to play (1-9): ")))-1
                if 0 < square < 9:
                    if board.get_index(square) == " ":
                        board.set_index(square, c_player.get_symbol())
                        run2 = 0
                    else:
                        print("That square is already taken, please pick again")
                else:
                    print("Invalid grid square, please pick again")
        board.play()
        if board.victory(c_player.get_symbol()) == True: #check if anybody has won
            print(f"{c_player.name} is the winner. Congratulations!")
            run = 0
        elif board.check() == True:     # check if there are any empty squares, if not then it's a draw
            print("Game over! It's a draw!")
            run = 0
    keep_playing = input("\nWould you like to continue playing? (Y/N): ").upper()
    if keep_playing == "Y": # loops back up to "playing" to start a new round
        print(f"\nEnjoy your next game, {p1.name} and {p2.name}!\n") 
    elif keep_playing == "N": # breaks loop to end script
        print("\nThanks for playing! Good bye!")
        playing = False
    else:
        print("Invalid input, please try again")