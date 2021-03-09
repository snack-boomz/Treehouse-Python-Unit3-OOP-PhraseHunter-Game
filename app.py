"""
Python Web Development Techdegree
Project 3 - Phrase Hunter Game
Author: Trey Annis
Goal: Meet All 'Exceeds Expectations' Requirements
--------------------------------
"""

from phrasehunter.game import Game


if __name__ == "__main__":
    
    while True:
        new_game = Game()
        new_game.start()

        if new_game.start() == 'Y':
            new_game = Game()
            new_game.start()
        
        else:
            exit()