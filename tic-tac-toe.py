# Function to print Tic Tac Toe Board
def draw_board_list(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |   {}".format(board[6], board[7], board[8]))
    print('\t_____|_____|______')


    print("\t     |     |")
    print("\t  {}  |  {}  |   {}".format(board[3], board[4], board[5]))
    print('\t_____|_____|______')


    print("\t     |     |")
    print("\t  {}  |  {}  |    {}".format(board[0], board[1], board[2]))
    print("\t     |     |")
    print("\n")
# End of function
# list_board = ['1','2','3','4','5','6','7','8','9']
# draw_board_list(list_board)

def check_winner(board):
    # All possible win combinations
    wins = [
        [0, 1, 2], # Row 1
        [3, 4, 5], # Row 2
        [6, 7, 8], # row 3
        [0, 3, 6], # colemn 1
        [1, 4, 7], # colemn 2
        [2, 5, 8], # colemn 3
        [0, 4, 8], # diagonal
        [2, 4, 6], # diagonal
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a] # Returns "X" or "O"
    if " " not in board:
        return "draw"
    return None # game is still ongoing

         
   
      
# to be continued

# The main game function
def game():
   
   cur_player = 'X'
   list_board = ['1','2','3','4','5','6','7','8','9']
   count = 1

    #repeat 11 - 1 = 10 times because that's the max number of moves a game can have (3x3=9)
   while count < 11:
      # draw_board_list(list_board)

      # #get current player's input
      # print("Move", count, "\n", "Player ", cur_player, "turn. Which square? : ", end="")
      # move = input()
       
     

      #    #convert str to int
      # move = int(move) -1

      while True:
         draw_board_list(list_board)
         player_input = input("Enter a number strictly between 1 and 9: ")
         if player_input.isdigit():
             player_input_int = int(player_input) 
             if 1 < player_input_int < 9:
                  print("Valid Input:", player_input_int)
                  
             else:
                  print("Input must be strictly between 1 and 9. Try again.")
                  continue
         else:
             print("Invalid input.Please enter a number.")
             continue

         move = player_input_int-1
         if list_board[move] != 'X' and list_board[move] != 'O':
            print()
         else:
            print("That cell is already filled.\nKey in another move?")
            continue       
         
         #update player's move on the list
         list_board[move] = cur_player

         #switch the current player
         if  cur_player =='X':
            cur_player = 'O'
         else:
            cur_player = 'X'

      

         if check_winner(list_board):
             print("winner???")

         count = count + 1

#main
game()
