"""Helper Functions"""


def draw_board(spots):
    """Draws board"""
    board = (f'|{spots[1]}|{spots[2]}|{spots[3]}|\n'
             f'|{spots[4]}|{spots[5]}|{spots[6]}|\n'
             f'|{spots[7]}|{spots[8]}|{spots[9]}|')
    print(board)

def check_turn(turn):
    return 'O' if turn % 2 == 0 else 'X'
