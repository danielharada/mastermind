"""Provides methods for getting user input for Mastermind game."""

import random

class MastermindUI:

    def __init__(self):
        self.keywords = {'help' : 'help', 'info' : 'info'}
        self.color_options = ('black', 'blue', 'green', 'red', 'white', 'yellow')
        print('Welcome to Mastermind in Python, written by Daniel Harada')
        self.info ='\nIn this game you are trying to break a 4 item code.  Each slot in the code will'\
              ' be filled by a colored peg. If you guess a color in the code in the correct position'\
              ' you will recieve a black result peg.  If you guess the correct color but in an incorrect'\
              ' location, you will recieve a white result peg. For each peg you guess which is not in the'\
              ' code, you recieve no result pegs.\n'
        print(self.info)
        print('If you have any questions, please type "help" or "info" at any time.  Good luck!\n') 

    def helpMe(self, keyword):
        help_with_spaces = '\nIn the base game there are 6 color options for code pegs: black, blue, green, red, '\
            'white, and yellow, which gives 1,296 possible 4 peg patterns. Adding space as an'\
            ' option(no peg placed) increases the number of possibilities to 2401. Please enter'\
            ' "yes" to allow spaces in the codes or "no" to disallow spaces.\n'

        help_with_guesses = '\nPlease pick a four color code as your guess. The possible colors are: {}.'\
              ' Each color in your code should be separated by a space.\n'.format(', '.join(self.color_options))

        help_generic = '\nThis is equal to the generic help message.  It should not be reached\n'

        help_keywords = {'help' : help_generic, 'help with spaces' : help_with_spaces, 'help with guesses' : help_with_guesses, 'info' : self.info}
        print(help_keywords[keyword])

    def userDecidesIfWithSpaces(self):
        self.keywords['help'] = 'help with spaces'
        while True:
            user_spaces_decision = input('Play with spaces?  Yes or No: ').lower()
            self.checkForKeywords(user_spaces_decision)
            if (user_spaces_decision == 'yes') or (user_spaces_decision == 'no'):
                break
        self.use_spaces = user_spaces_decision     

    def checkForKeywords(self, user_input):
        if user_input in self.keywords:
            self.helpMe(self.keywords[user_input])
            return True

    def setColorOptions(self):
        color_options = ['black', 'blue', 'green', 'red', 'white', 'yellow']
    
        if self.use_spaces == 'yes':
            color_options += ['space']

        self.color_options = tuple(color_options)

    def generateSolution(self):
        self.solution_pegs = tuple(random.choice(self.color_options) for x in range(4))

    def userInputsGuess(self):
        self.keywords['help'] = 'help with guesses'
        valid_guess = False
        while not valid_guess:
            user_input = input('Please enter your guess: ').lower()
            if not self.checkForKeywords(user_input):
                user_guess = tuple(user_input.split())
                valid_guess = validateGuess(user_guess)

        self.guess_pegs = user_guess
    
    def validateGuess(user_guess):
        if not (set(user_guess) < set(self.color_options)):
            print('Guess needs to only include colors from: ', ', '.join(self.color_options))        
        elif (len(user_guess) != 4):
            print('Please enter a 4 color guess, each color separated by a space')
        else:
            return True

    def userDecidesPlayAgain(self):
        play_again_TF = {'yes' : True, 'no' : False}
        while True:
            play_again = input('Would you like to play again?  Yes or No: ').lower()
            if (play_again == 'yes') or (play_again == 'no'):
                break
        return play_again_TF[play_again] 


if __name__ == '__main__':
    thisUI = MastermindUI()
    thisUI.userDecidesIfWithSpaces()
    thisUI.setColorOptions()
    thisUI.generateSolution()
    thisUI.userInputsGuess()
    play_again = thisUI.userDecidesPlayAgain()

    print(thisUI.color_options)
    print(thisUI.solution_pegs)
    print(thisUI.guess_pegs)
    print(play_again)


    

    
