import random
from phrasehunter.phrase import Phrase
class Game():

    def __init__(self):
        self.missed = 0
        # -- https://randomwordgenerator.com/ -- 
        self.phrases = ["price", "board", "court", "spoil", "graze"]
        self.active_phrase = None
        self.guesses = []
        

    def start(self):
        # Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, 
        # increments the number of missed by one if the guess is incorrect, calls the game_over method.
        self.welcome()
        random_phrase = self.get_random_phrase()
        print(random_phrase)
        new_phrase = Phrase(random_phrase)
        print(new_phrase)
        
        while True:
            user_guess = self.get_guess()
            print("User Guess: ", user_guess)
            print(self.guesses)
            
            if new_phrase.check_letter(user_guess) == False:
                self.missed += 1
                print("Incorrect Guesses: ", self.missed)
                if self.missed == 5:
                    self.game_over()
                    



    def get_random_phrase(self):
        # this method randomly retrieves one of the phrases stored in the phrases list and returns it.
        return random.choice(self.phrases)

    def welcome(self):
        print("""

    ╭━━━╮╱╱╱╭╮╭╮╱╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╭╮╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭╮╱╱╱╭╮╱╭━━━╮
    ┃╭━╮┃╱╱╭╯╰┫┃╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱┃┃╱╱╭╯╰╮┃╭━╮┃
    ┃╰━╯┣╮╱┣╮╭┫╰━┳━━┳━╮╱╰╯┃┃┣┻━┳━━┫╰━┳━╯┣━━┳━━┳━┳━━┳━━╮┃┃╱┃┣━╮┣╮╭╯╰╯╭╯┃
    ┃╭━━┫┃╱┃┃┃┃╭╮┃╭╮┃╭╮╮╱╱┃┃┃┃━┫╭━┫╭╮┃╭╮┃┃━┫╭╮┃╭┫┃━┫┃━┫┃┃╱┃┃╭╮╋┫┃╱╭━╯╭╯
    ┃┃╱╱┃╰━╯┃╰┫┃┃┃╰╯┃┃┃┃╱╱┃┃┃┃━┫╰━┫┃┃┃╰╯┃┃━┫╰╯┃┃┃┃━┫┃━┫┃╰━╯┃┃┃┃┃╰╮┃┃╰━╮
    ╰╯╱╱╰━╮╭┻━┻╯╰┻━━┻╯╰╯╱╱╰╯╰━━┻━━┻╯╰┻━━┻━━┻━╮┣╯╰━━┻━━╯╰━━━┻╯╰┻┻━╯╰━━━╯
    ╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
    ╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯                                                                                                                                                                                                
    """, "\n")
        print("== Welcome to Phrase Hunters. ==")

    def get_guess(self):
        user_guess = input("Guess a letter: ")
        return user_guess


    def game_over(self):
        print("you have failed humanity.")
        exit(0)
    