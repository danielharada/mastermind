"""mastermind.py:  Text based version of Mastermind
See http://en.wikipedia.org/wiki/Mastermind_(board_game) for game info
or type 'info' at any prompt during the game 
"""

import mastermindUI
import mastermindGameState

def runGame():
    play_again = True
    while play_again:
        game_over = False

        game_UI = mastermindUI.MastermindUI()
        setColors(game_UI)
        game_UI.generateSolution()
        solution_pegs = game_UI.solution_pegs
        game_state = mastermindGameState.MastermindGameState(solution_pegs)
        max_guesses = game_state.max_guesses
        
        while not game_over:
            game_over, win = executeOneTurn(game_UI, game_state)

        gameEndMessage(win, solution_pegs)
        play_again = game_UI.userDecidesPlayAgain()

def setColors(game_UI):
    game_UI.userDecidesIfWithSpaces()
    game_UI.setColorOptions()

def executeOneTurn(game_UI, game_state):
    game_UI.userInputsGuess()
    guess_pegs = game_UI.guess_pegs
    game_state.newGuess(guess_pegs)
    game_state.assignResultPegs()
    game_state.printResult()          

    game_over, win = game_state.evaluateGameOver()

    game_state.prepareForNewGuess()
    
    return game_over, win

def gameEndMessage(win, solution_pegs):
    if win:
        print('Congratulations! You broke the code!')
    else:
        print('Sorry, you were unable to break the code in {} guesses.'.format(max_guesses))

    print('The solution was ', solution_pegs)

def printGuessHistory(game_state):
    for i in range(1,game_state.current_guess_number):
        print('Guess {} was'.format(i), game_state.history['guess{}'.format(i)],
                'and the result was', game_state.history['result{}'.format(i)])

if __name__ == '__main__':       
    runGame()



