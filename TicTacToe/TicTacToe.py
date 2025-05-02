# Function for printing a visual board

def print_board(board):
    
    for i, row in enumerate(board[::-1]):
        print(" | ".join(row))
        if (i < len(board) - 1):
            print("-" * (3 * len(row)))

def symbol_input(choice):
        while (choice.lower() != "x") and (choice.lower() != "o"):
            choice = input("Please choose from 'X's or 'O's : ")

        return(choice)

def take_move():

    choice = "Error"
    within_range = False

    while (choice.isdigit() != True) or (within_range == False):
        choice = input("Where would you like to make your move? (1 - 9) : ")

        if choice.isdigit() == False:
            print("!!! Selection must be a number (1 - 9)!!!")
        elif choice.isdigit() == True:
            if int(choice) in range(1,10):
                within_range = True
            else:
                print("!!! Number must be between (1 - 9)!!!")
        
    return int(choice)

def co_ordinates(num):
    row = int((num - 1) / 3)
    column = int((num - 1) % 3)
    return (row, column)

def victory_check(board):
    victory = False    
    for x in range(0,3):
        if (board[x][0] == board[x][1] == board[x][2] != " "):
            print("Win Horizontal")
            victory = True
            return victory   
        elif (board[0][x] == board[1][x] == board[2][x] != " "):
            print("Win Vertical")
            victory = True
            return victory    
    if (board[0][0] == board[1][1] == board[2][2] != " ") or (board[2][0] == board[1][1] == board[0][2] != " "):
        print("Win Diagonal")
        victory = True
        return victory
    else:
        return victory

  def tic_tac_toe():
    '''
    Game for 2 human players sitting at the same computer.
    
    Board printed every time player makes  move
    
    Accept input and place symbol on the board - Make sure cannot input on a filled in space
    
    7 | 8 | 9
    4 | 5 | 6
    1 | 2 | 3
    
    Player 1: X or O?
    
    Checks for win condition
    
    Play again?
    '''
    from IPython.display import clear_output

    print("Welcome to Tic-Tac-Toe!")
    start = "Y"
    
    while (start.lower() == "y"):
        start = input("Ready to start a new game? (Y/N) : ")
        if (start.lower() == "y"):
            
            x_marker = False
            player_one_turn = True
            position_markers = [["1" , "2" , "3"], ["4" , "5" , "6"],["7" , "8" , "9"]]
            board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
            victory = False
            
            possibile_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            turns_taken = []
        
        
            # Display Starting Menu        
            player_one = input("Player 1, please enter your name : ")
            player_two = input("Player 2, please enter your name : ")
        
            choice = input(f"{player_one} would you like to be 'X's or 'O's? : ")
            symbol_input(choice)   
            # Need to validate symbol input
        
            # Set marker. If choice = x, marker = True for P1
            if choice.lower() == "x":
                x_marker = True
        
            print("\n Please use the following as your guide;\n")
            print_board(position_markers)
        
            # Take user choice to place symbol. Cannot be previously taken
            while (victory == False) and (len(possibile_choices)!=0):
                choice = int(take_move())
                while choice not in possibile_choices:
                    choice = int(input("That square has already been marked. Please pick a different square : "))
                else:
                    possibile_choices.remove(choice)
                    turns_taken.append(choice)
                    
                co_ords = co_ordinates(choice)
        
            # While loop until victory == True, or all spots taken
                if (x_marker == True):
                    board[co_ords[0]][co_ords[1]] = "X"
                    x_marker = False
                    player_one_turn = not player_one_turn
                    clear_output(wait=False)
                    print_board(position_markers)
                    print("\n")
                    print_board(board)
                    victory = victory_check(board)
                else:
                    board[co_ords[0]][co_ords[1]] = "O"
                    x_marker = True
                    player_one_turn = not player_one_turn
                    clear_output(wait=False)
                    print_board(position_markers)
                    print("\n")
                    print_board(board)
                    victory = victory_check(board)
        
            if (victory == True) and (player_one_turn == False):
                print(f"{player_one} has won!")
            elif (victory == True) and (player_one_turn == True):
                print(f"{player_two} has won!")
            elif (possibile_choices == []):
                print("It looks like a draw.")

    else:
        print("Have a good day, and see you next time!")
