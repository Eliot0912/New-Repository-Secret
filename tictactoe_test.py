import pytest
from tictactoe import TicTacToe

def test_initial_board():
    game = TicTacToe()
    assert game.board == [' ' for _ in range(9)]
    assert game.current_winner is None

def test_make_move():
    game = TicTacToe()
    assert game.make_move(0, 'X')
    assert game.board[0] == 'X'
    assert not game.make_move(0, 'O')

def test_winner_row():
    game = TicTacToe()
    game.make_move(0, 'X')
    game.make_move(1, 'X')
    game.make_move(2, 'X')
    assert game.current_winner == 'X'

def test_winner_column():
    game = TicTacToe()
    game.make_move(0, 'O')
    game.make_move(3, 'O')
    game.make_move(6, 'O')
    assert game.current_winner == 'O'

def test_winner_diagonal():
    game = TicTacToe()
    game.make_move(0, 'X')
    game.make_move(4, 'X')
    game.make_move(8, 'X')
    assert game.current_winner == 'X'

def test_no_winner():
    game = TicTacToe()
    game.make_move(0, 'X')
    game.make_move(1, 'O')
    game.make_move(2, 'X')
    game.make_move(3, 'O')
    game.make_move(4, 'X')
    game.make_move(5, 'O')
    game.make_move(6, 'O')
    game.make_move(7, 'X')
    game.make_move(8, 'O')
    assert game.current_winner is None