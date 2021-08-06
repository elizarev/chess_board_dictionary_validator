import pytest
import functions


def test_validate_valid_chess_position():
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    # Act / When
    validator = functions.valid_chess_position(chessboard)
    # Assert / Then
    expected = True
    assert validator == expected


def test_validate_invalid_chess_position():
    # Arrange / Given
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'z9': 'brook',
    }
    # Act / When
    validator = functions.valid_chess_position(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_colours_and_pieces():
    # Arrange / Given
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    # Act / When
    validator = functions.valid_colours_and_pieces(chessboard)
    # Assert / Then
    expected = True
    assert validator == expected


def test_validate_invalid__colours_and_pieces():
    # Arrange / Given
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'zflower', 'h8': 'brook',
    }
    # Act / When
    validator = functions.valid_colours_and_pieces(chessboard)
    # Assert / pThen
    expected = False
    assert validator == expected


def test_count_number_of_pieces():
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wqueen',
        'd1': 'wqueen', 'e8': 'wrook', 'f8': 'bbishop',
        'g8': 'bknight', 'h8': 'brook', 'h1': 'wrook',
    }
    # Act / When
    validator = functions.number_of_pieces(chessboard)
    # Assert / Then
    expected = {
        'wrook': 3, 'wknight': 1, 'wqueen': 2,
        'bbishop': 1, 'bknight': 1, 'brook': 1,
        'total_black_pieces': 3, 'total_white_pieces': 6
    }
    assert validator == expected


def test_validate_invalid_number_of_bpawns():
    # Arrange / Given
    chessboard = {
        'a2': 'bpawn', 'b2': 'bpawn',
        'c2': 'bpawn', 'd2': 'bpawn',
        'e2': 'bpawn', 'f2': 'bpawn',
        'g2': 'bpawn', 'h2': 'bpawn',
        'g3': 'bpawn', 'h3': 'bpawn',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_invalid_number_of_wpawns():
    # Arrange / Given
    chessboard = {
        'a2': 'wpawn', 'b2': 'wpawn',
        'c2': 'wpawn', 'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',
        'g2': 'wpawn', 'h2': 'wpawn',
        'g3': 'wpawn', 'h3': 'wpawn',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_invalid_number_of_bkings():
    # Arrange / Given
    chessboard = {'a1': 'bking', 'c6': 'bking'}
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_invalid_number_of_wkings():
    # Arrange / Given
    chessboard = {'c7': 'wking', 'd6': 'wking'}
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_invalid_number_of_bqueens():
    # Arrange / Given
    chessboard = {
        'a1': 'bqueen', 'b1': 'bqueen',
        'c1': 'bqueen', 'd1': 'bqueen',
        'e1': 'bqueen', 'f1': 'bqueen',
        'g1': 'bqueen', 'h1': 'bqueen',
        'a2': 'bqueen', 'b2': 'bqueen',
        'c3': 'bqueen', 'd4': 'bqueen',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_invalid_number_of_wqueens():
    # Arrange / Given
    chessboard = {
        'a1': 'wqueen', 'b1': 'wqueen',
        'c1': 'wqueen', 'd1': 'wqueen',
        'e1': 'wqueen', 'f1': 'wqueen',
        'g1': 'wqueen', 'h1': 'wqueen',
        'a2': 'wqueen', 'b2': 'wqueen',
        'c3': 'wqueen', 'd4': 'wqueen',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_invalid_number_of_brooks():
    # Arrange / Given
    chessboard = {
        'a1': 'brook', 'b1': 'brook',
        'c1': 'brook', 'd1': 'brook',
        'e1': 'brook', 'f1': 'brook',
        'g1': 'brook', 'h1': 'brook',
        'a2': 'brook', 'b2': 'brook',
        'c3': 'brook', 'd4': 'brook',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_invalid_number_of_wrooks():
    # Arrange / Given
    chessboard = {
        'a8': 'wrook', 'b8': 'wrook',
        'c8': 'wrook', 'd8': 'wrook',
        'e8': 'wrook', 'f8': 'wrook',
        'g8': 'wrook', 'h8': 'wrook',
        'a7': 'wrook', 'b7': 'wrook',
        'c7': 'wrook', 'd7': 'wrook',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_valid_number_of_white_pieces():
    # Arrange / Given
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = True
    assert validator == expected


def test_validate_invalid_number_of_blacks_pieces():
    # Arrange / Given
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'bking', 'f1': 'bbishop', 'g1': 'bknight', 'h1': 'brook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_invalid_number_of_white_pieces():
    # Arrange / Given
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'wrook', 'b8': 'wknight', 'c8': 'wbishop', 'd8': 'wqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    # Act / When
    validator = functions.valid_number_of_pieces(chessboard)
    # Assert / Then
    expected = False
    assert validator == expected


def test_validate_chess_board_with_valid_positions():
    chessboard = {
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    validator = functions.valid_chess_board(chessboard)
    expected = True
    assert validator == expected


def test_valid_chess_board_invalid_positions():
    chessboard = {
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'z8': 'brook',
    }
    validator = functions.valid_chess_board(chessboard)
    expected = False
    assert validator == expected


def test_valid_chess_board_valid_amount():
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    validator = functions.valid_chess_board(chessboard)
    expected = True
    assert validator == expected


def test_valid_chess_board_invalid_amount():
    chessboard = {
        'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
        'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
        'a2': 'wpawn', 'b2': 'wpawn',  'c2': 'wpawn',   'd2': 'wpawn',
        'e2': 'wpawn', 'f2': 'wpawn',  'g2': 'wpawn',   'h2': 'wpawn',
        'a7': 'bpawn', 'b7': 'bpawn',  'c7': 'bpawn',   'd7': 'bpawn',
        'e7': 'bpawn', 'f7': 'bpawn',  'g7': 'bpawn',   'h7': 'bpawn',
        'a8': 'wrook', 'b8': 'wknight', 'c8': 'wbishop', 'd8': 'wqueen',
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    validator = functions.valid_chess_board(chessboard)
    expected = False
    assert validator == expected


def test_validate_chess_board_with_invalid_pieces():
    chessboard = {
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': '6rook',
    }
    validator = functions.valid_chess_board(chessboard)
    expected = False
    assert validator == expected


def test_validate_chess_board_with_valid_pieces():
    chessboard = {
        'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
    }
    validator = functions.is_valid_chess_board(chessboard)
    expected = True
    assert validator == expected
