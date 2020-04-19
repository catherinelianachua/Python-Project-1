#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:15:57 2020

@author: catherinelianazhengchua
"""

#global variables
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

game_still_going = True

winner = None

current_player = "X"



def display_board():
    print(board[0]+ " | "  +board[1]+ " | " + board[2])
    print(board[3]+ " | "  +board[4]+ " | " + board[5])
    print(board[6]+ " | "  +board[7]+ " | " + board[8])
    
display_board()


def play_game():
    display_board()
    
    
    #loop through turns til the game is over(either someone wins or tie)
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    
    if winner == " X " or winner == " O ":
        print (winner + "won.")
    elif winner == None: 
        print("Tie.")
    
        
    
def handle_turn(player):
    print(player + "'s turn." )
    position = input("Choose a position from 1-9: ")
    
    valid = False 
    while not valid:
       
       while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
           position = input("Choose a position from 1-9: ")

    
    position = int(position) - 1
    
    if board[position] == "-":
        valid = True
    else:
        print("You can't go there, try again")
    
    
    board[position] = player
    
    display_board()
    

def check_if_game_over():
    check_for_winner()
    check_if_tie()
    

def check_for_winner():
               
    #setup global variables           
    global winner 
               
    #row winner
    row_winner = check_rows()
    #column winner
    column_winner = check_columns()
    #diagonal winner
    diagonal_winner = check_diagonals()
               
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return
               

def check_rows():
    #setup global variables 
    global game_still_going
    #check if rows have the same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    #check if game is still ongoing
    if row_1 or row_2 or row_3:
        game_still_going = False
               
    #return the winner X or 0
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]   
               
    return

def check_columns():
    #setup global variables 
    global game_still_going
    #check if rows have the same value and is not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    #check if game is still ongoing
    if column_1 or column_2 or column_3:
        game_still_going = False
               
    #return the winner X or 0
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]   
    return
               
def check_diagonals():
    #setup global variables 
    global game_still_going
    #check if rows have the same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    
    #check if game is still ongoing
    if diagonal_1 or diagonal_2:
        game_still_going = False
               
    #return the winner X or 0
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return
               
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    #global variables
    global current_player 
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
