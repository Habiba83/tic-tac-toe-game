# build the game board
board=[
        ["","",""],
        ["","",""],
        ["","",""]
]
#list of odd num
odd=[1,3,5,7,9]
#list of even nums 
even=[0,2,4,6,8]
#display the game board
def display_board():
   for row in board:
       print(row[0] ,"|",row[1] , "|" ,row[2] , "|" )
       print("--------------")
#the first user input 
def first_user_input():
    #checking the num of and coulmn
    row=int(input("first player enter the num of row:"))
    coulmn=int(input("enter the num of coulmn:"))
    #taking rhe player num 
    player_input=int(input("enter an odd between 0 to 9"))
    while row not in range (0,3) or coulmn not in range(0,3) or board[row][coulmn]!="" or player_input not in odd:
                   print("not_valid")
                   row=int(input("first player enter the num of row from 0-2:"))
                   coulmn=int(input("enter the num of coulmn from 0-2:"))
                   player_input=int(input("enter an odd between 0 to 9:"))
    board[row][coulmn]= player_input
    odd.remove(player_input)#remove the num from the list
    display_board()
def second_user_input():
    #checking the num of and coulmn
    row=int(input("second player enter the num of row:"))
    coulmn=int(input("enter the num of coulmn:"))
     #taking rhe player num 

    player_input=int(input("enter an even between 0 to 9"))
    while row not in range (0,3) or coulmn not in range(0,3) or board[row][coulmn]!="" or player_input not in even:
                   print("not_valid")
                   row=int(input("second player enter the num of row:"))
                   coulmn=int(input("enter the num of coulmn:"))
                   player_input=int(input("enter an even between 0 to 9:"))
    board[row][coulmn]= player_input
    even.remove(player_input)#remove the num from even nums
    display_board()
#checking the winner 
def winner(): 
    for row in board:
        if "" in row:
            break
#checking the sum of rows 
 
        elif sum(row) == 15: 
            return True
#checking the sum of coulmns
    for i in range(3):  
        column_sum = 0 
        for j in range(3): 
            if board[j][i] == "": 
                break 
            else: 
                column_sum += board[j][i] 
            if column_sum == 15: 
                return True
#checking the sum of left diagnol
    diagonal_sum = 0 
    for x in range(3):  
        if board[x][x] == "": 
            break 
        diagonal_sum += board[x][x] 
        if diagonal_sum == 15: 
            return True
#check the sum of the right diagnol 
    diagonal_sum = 0 
    for y in range(3):  
        if board[y][2 - y] == "": 
            break 
        diagonal_sum += board[y][2 - y] 
        if diagonal_sum == 15: 
            return True 
    return False 
 
#check if no winner  
def draw(): 
    for i in board: 
        if "" in i: 
            return False 
    return True 
 
#the main function  
def tic_tac_toe(): 
       while True: 
        display_board() 
        first_user_input() 
        if winner(): 
            display_board() 
            print("the first player is the winner ") 
            return 0 
        display_board()  
        second_user_input()
        if winner(): 
            display_board() 
            print("the second user is the winner ")
            return 0
        if draw(): 
            display_board() 
            print("Draw") 
            return 0   
        
tic_tac_toe() 

