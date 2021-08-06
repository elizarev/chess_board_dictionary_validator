import functions

chessboard_1 = {
    'a1': 'wrook', 'a2': 'wpawn', 'b2': 'wpawn',
    'd6': 'bpawn', 'e6': 'bpawn', 'a7': 'bpawn',
    'd4': 'wpawn', 'f4': 'bqueen', 'c6': 'bpawn',
    'h2': 'wking', 'b3': 'wbishop', 'c3': 'wpawn',
    'b7': 'bpawn', 'd7': 'bking', 'g7': 'bbishop',
}

chessboard_2 = {
    'a1': 'wrook', 'a2': 'wpawn', 'b2': 'wpawn',
    'd6': 'bpawn', 'e6': 'bpawn', 'a7': 'bpawn',
    'd4': 'wpawn', 'f4': 'bqueen', 'c6': 'bpawn',
    'h2': 'wking', 'b3': 'wbishop', 'c3': 'wpawn',
    'b7': 'bpawn', 'd7': 'bking', 'g89': 'zbishop',
}

print(functions.is_valid_chess_board(chessboard_1))
print(functions.is_valid_chess_board(chessboard_2))
