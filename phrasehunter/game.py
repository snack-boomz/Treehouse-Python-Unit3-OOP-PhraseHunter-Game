import random
from phrasehunter.phrase import Phrase
class Game():

    def __init__(self):
        self.missed = 0
        # -- https://randomwordgenerator.com/ -- 
        self.phrases = [Phrase("hello world"), Phrase("Amazing pie"), Phrase("Black cat"), Phrase("Sparkling water"), Phrase("large chair")]
        self.active_phrase = None
        self.guesses = []
        

    def start(self):
        # Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, 
        # increments the number of missed by one if the guess is incorrect, calls the game_over method.
        
        # Upon new game, reset values 
        self.guesses = []
        self.active_phrase = None
        self.missed = 0
        
        self.welcome()
        random_phrase = self.get_random_phrase()
        new_phrase = random_phrase
        new_phrase.active_phrase = random_phrase
        
        
        
        while True:
            new_phrase.display()
            
            if new_phrase.check_complete():
                print("\nYou won! You have guessed the phrase!")
                # Referenced from Unit 1 Project
                loop = 1
                while loop:
                    play_again = input("Would you like to play again? (Y/N): ")
                    play_again = play_again.upper()
                    if play_again == 'Y':
                        return play_again
                    elif play_again == 'N':
                        quit()
                    else:
                        print("Please enter Y or N.")

                
            user_guess = self.get_guess()
            
            self.guesses.append(user_guess)
            print("Current guesses: ", self.guesses, "\n")

            

            if new_phrase.check_letter(user_guess) == False:
                self.missed += 1
                print("\nIncorrect!")
                print("Incorrect Guesses: ", self.missed, "\n")
                if self.missed == 5:
                    if self.game_over() == True:
                        loop = 1
                        while loop:
                            play_again = input("Would you like to play again? (Y/N): ")
                            play_again = play_again.upper()
                            if play_again == 'Y':
                                return play_again
                            elif play_again == 'N':
                                quit()
                            else:
                                print("Please enter Y or N.")
                    



    def get_random_phrase(self):
        # this method randomly retrieves one of the phrases stored in the phrases list and returns it.
        return random.choice(self.phrases)

    def welcome(self):
        print("""

        ╭━━━╮╱╱╱╭╮╭╮╱╱╱╱╱╱╱╱╭━━━━╮╱╱╱╱╭╮╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╭╮╱╱╱╭╮╱╭━━━╮
        ┃╭━╮┃╱╱╭╯╰┫┃╱╱╱╱╱╱╱╱┃╭╮╭╮┃╱╱╱╱┃┃╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱┃┃╱╱╭╯╰╮┃╭━╮┃
        ┃╰━╯┣╮╱┣╮╭┫╰━┳━━┳━╮╱╰╯┃┃┣┻━┳━━┫╰━┳━╯┣━━┳━━┳━┳━━┳━━╮┃┃╱┃┣━╮┣╮╭╯╰╯╭╯┃
        ┃╭━━┫┃╱┃┃┃┃╭╮┃╭╮┃╭╮╮╱╱┃┃┃┃━┫╭━┫╭╮┃╭╮┃┃━┫╭╮┃╭┫┃━┫┃━┫┃┃╱┃┃╭╮╋┫┃╱╭╮╰╮┃
        ┃┃╱╱┃╰━╯┃╰┫┃┃┃╰╯┃┃┃┃╱╱┃┃┃┃━┫╰━┫┃┃┃╰╯┃┃━┫╰╯┃┃┃┃━┫┃━┫┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃
        ╰╯╱╱╰━╮╭┻━┻╯╰┻━━┻╯╰╯╱╱╰╯╰━━┻━━┻╯╰┻━━┻━━┻━╮┣╯╰━━┻━━╯╰━━━┻╯╰┻┻━╯╰━━━╯
        ╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
        ╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯                                                                                                                                                                              
    """, "\n")
        print("== Welcome to Phrase Hunters. ==\n")

    def get_guess(self):
        guessing = True
        while guessing:
        # referenced from Unit 1 Project
            try:
                user_guess = input("\n\nGuess a letter: ").lower()
                if len(user_guess) > 1:
                    raise ValueError("Your guess guess is longer than a single letter. Please enter a single letter.")
                elif user_guess.isalpha() == False:
                    raise ValueError("Your guess is not a string/character. Please enter a string character.")
                
                for character in self.guesses:
                    if character == user_guess:
                        raise ValueError("You've already guessed this character, try another character.")
            # raise
            # except
            except ValueError as err:
                print("That guess is not valid. Please enter a valid guess.")
                print("Error: {}".format(err))
            else:
                return user_guess


    def game_over(self):
        print("you have failed humanity.")
        return True
    