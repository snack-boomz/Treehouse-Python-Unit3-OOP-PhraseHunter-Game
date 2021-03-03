class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.is_guessed = False
        self.display_table = []

    def __str__(self):
        return self.phrase

    def display(self):
        # this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores. 
        # For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
        # the output should look like this: _ _ _ _ o    _ o _ _ _
        print(self.display_table)
        
 

    def check_letter(self, guess):
        # checks to see if the letter selected by the user matches a letter in the phrase.
        phrase_characters = list(self.phrase)
        from game import Game
        for character in phrase_characters:
            
            if guess == character:
                self.display_table.append(character)
                return True
            else:
                self.display_table.append("_")
                return False


    def check_complete(self):
        complete = False
        for character in self.display().display:
            if character == "_":
                complete = False
            else:
                continue
        if complete == True:
            return True
        else:
            return False
