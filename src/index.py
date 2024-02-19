"""
Used to start the application
"""

from services.ai import AI
from services.board import Board
from services.logic import Logic
from ui import UI

if __name__ == "__main__":
    game_board = Board()
    game_logic = Logic()
    cpu = AI()
    ui = UI(game_board, game_logic, cpu)
    ui.start_game()
