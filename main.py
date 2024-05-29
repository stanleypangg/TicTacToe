"""Tic Tac Toe"""
from helpers import draw_board, check_turn
import os

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

turn = 0
playing = True

while playing:
    turn += 1
    # Reset the screen
    os.system('cls')
    draw_board(spots)
    # Get input from player
    choice = input()
    # Player quits
    if choice == "q":
        playing = False
    elif int(choice) in spots:
        spots[int(choice)] = check_turn(turn)
