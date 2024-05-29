"""Tic Tac Toe"""
from helpers import draw_board, check_turn
from time import sleep
import os

spots = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

turn = 0
playing = True

while playing:
    print("Player X's Turn") if check_turn(turn) == "X" else print("Player O's Turn")
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # Get input from player
    choice = input()
    # Player quits
    if choice == "q":
        playing = False
    # Player inputs valid choice
    elif choice.isdigit() and int(choice) in spots:
        # Checks for unoccupied space
        if spots[int(choice)] == ' ':
            spots[int(choice)] = check_turn(turn)
            turn += 1
        else:
            print("Already occupied space!")
            sleep(0.5)
