def valid_chess_position(chessboard):
    chess_position = [
        'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
        'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
        'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
        'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
        'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
        'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
    ]
    for k in chessboard.keys():
        if k not in chess_position:
            return False
    return True


def valid_colours_and_pieces(chessboard):
    chess_pieces = [
        'bking', 'brook', 'bpawn',
        'wking', 'wrook', 'wpawn',
        'wqueen', 'wbishop', 'wknight',
        'bqueen', 'bbishop', 'bknight',
    ]
    for v in chessboard.values():
        if v not in chess_pieces:
            return False
    return True


def number_of_pieces(chessboard):
    total_pieces = {'total_black_pieces': 0, 'total_white_pieces': 0}
    for piece in chessboard.values():
        total_pieces[piece] = total_pieces.get(piece, 0) + 1
        if piece[0:1] == 'b':
            total_pieces['total_black_pieces'] += 1
        if piece[0:1] == 'w':
            total_pieces['total_white_pieces'] += 1
    return total_pieces


def valid_number_of_pieces(chessboard):
    maximum = {'bking': 1, 'brook': 10, 'bpawn': 8,
               'wking': 1, 'wrook': 10, 'wpawn': 8,
               'wqueen': 9, 'wbishop': 10, 'wknight': 10,
               'bqueen': 9, 'bbishop': 10, 'bknight': 10,
               'total_white_pieces': 16, 'total_black_pieces': 16,
               }
    total = (number_of_pieces(chessboard))
    for piece, amount in total.items():
        if amount > maximum[piece]:
            return False
    return True


def is_valid_chess_board(chessboard):
    return valid_chess_position(chessboard)\
        and valid_colours_and_pieces(chessboard)\
        and valid_number_of_pieces(chessboard)
