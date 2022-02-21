# Chess Dictionary Validator.

This is my answer to the Practice Project: Chess Dictionary Validator from the book Automate the Boring Stuff Chapter 5.

The specifications were:
Write a function that takes a dictionary argument and returns True or False depending on if the board is valid. The function checks for the correct amount of pieces, the valid position on the board and valid names for the pieces.

I have changed the notation of the position of the pieces sugested in the book e.g from '1h' to 'h1'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. The function detects when a bug has resulted in an improper chess board.

I have used pytest for all the tests.
