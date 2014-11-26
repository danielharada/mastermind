import mastermindUI
import mastermindGameState

def runGame():
    play_again = True
    while play_again:
        game_over = False

        this_game_UI = mastermindUI.MastermindUI()
        this_game_UI.userDecidesIfWithSpaces()
        this_game_UI.setColorOptions()
        this_game_UI.generateSolution()
        solution_pegs = this_game_UI.solution_pegs
        
        this_game_state = mastermindGameState.MastermindGameState(solution_pegs)
        max_guesses = this_game_state.max_guesses
        
        while not game_over:
            this_game_UI.userInputsGuess()
            guess_pegs = this_game_UI.guess_pegs
            this_game_state.newGuess(guess_pegs)
            this_game_state.assignResultPegs()
            this_game_state.printResult()          

            game_over, win = this_game_state.evaluateGameOver()

            this_game_state.prepareForNewGuess() 

        if win:
            print('Congratulations! You broke the code!')
        else:
            print('Sorry, you were unable to break the code in {} guesses.'.format(max_guesses))

        print('The solution was ', this_game_state.solution['pegs'])
        
        for i in range(1,this_game_state.current_guess_number):
            print('Guess {} was'.format(i), this_game_state.history['guess{}'.format(i)],\
                  'and the result was', this_game_state.history['result{}'.format(i)])

        play_again = this_game_UI.userDecidesPlayAgain()

if __name__ == '__main__':       
    runGame()



