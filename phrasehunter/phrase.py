
class Phrase:
    arbitrary_value = 0

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.is_guessed = False
        self.display_table = ["_", "_", "_", "_", "_"]

    def __str__(self):
        return self.phrase
        

    def display(self):
        # this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores. 
        # For example, if the current phrase is "hello world" and the user has guessed the letter "o", 
        # the output should look like this: _ _ _ _ o    _ o _ _ _
        
        #phrase_characters = list(self.phrase)

        #if self.arbitrary_value == 0:
        #    for character in phrase_characters:
        #        self.display_table.append(character)
        #    self.arbitrary_value = 1
        print(self.display_table)
        
 

    def check_letter(self, guess):
        # checks to see if the letter selected by the user matches a letter in the phrase.
        phrase_characters = list(self.phrase)
        print("check_letter method: ", phrase_characters)
        print("Check_letter method guess: ", guess)
        #for character in phrase_characters:

        if guess == phrase_characters[0]:
            self.display_table[0] = guess
        if guess == phrase_characters[1]:
            self.display_table[1] = guess
        if guess == phrase_characters[2]:
            self.display_table[2] = guess
        if guess == phrase_characters[3]:
            self.display_table[3] = guess
        if guess == phrase_characters[4]:
            self.display_table[4] = guess
        
        counter = 0
        for character in phrase_characters:
            if guess != character:
                counter += 1
                if counter == 5:
                    return False

    def check_complete(self):
        complete = True
        for character in self.display_table:
            if character == "_":
                complete = False
            else:
                continue
        if complete == True:
            return True
        else:
            return False
