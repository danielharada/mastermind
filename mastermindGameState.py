class MastermindGameState:

    def __init__(self, solution_pegs):

        self.peg_is_used_default = (False, False, False, False)
        self.current_guess_number = 1
        self.max_guesses = 10
        self.history = {}
        self.result = {}
        self.guess = {}
        self.solution = {}

        self.resetResultPegs()
        self.resetUsedPegs()

        self.solution['pegs'] = solution_pegs

    def resetUsedPegs(self):
        self.guess['pegIsUsed'] = list(self.peg_is_used_default)
        self.solution['pegIsUsed'] = list(self.peg_is_used_default)

    def resetResultPegs(self):
        self.result['black pegs'] = 0
        self.result['white pegs'] = 0

    def newGuess(self, guess_pegs):
        self.guess['pegs'] = guess_pegs

        
    def prepareForNewGuess(self):
        self.archiveGuess()
        self.archiveResult()
        self.resetResultPegs()
        self.resetUsedPegs()
        self.current_guess_number += 1

    def archiveGuess(self):
        self.history['guess{}'.format(self.current_guess_number)] = self.guess['pegs']

    def archiveResult(self):
        self.history['result{}'.format(self.current_guess_number)] = {}
        self.history['result{}'.format(self.current_guess_number)]['black pegs'] = self.result['black pegs']
        self.history['result{}'.format(self.current_guess_number)]['white pegs'] = self.result['white pegs']     

    def assignResultPegs(self):
        is_guess_correct = self.checkGuessAgainstSolution()
        if is_guess_correct:
            self.result['black pegs'] = 4
            self.result['white pegs'] = 0
        else:
            self.updateBlackResultPegsAndUsedPegs()
            self.updateWhiteResultPegsAndUsedPegs()

    def checkGuessAgainstSolution(self):
        return self.guess['pegs'] == self.solution['pegs']

    def updateBlackResultPegsAndUsedPegs(self):
        black_pegs = 0

        for guess_peg_index in range(4):
            if self.checkPegsMatched(guess_peg_index, guess_peg_index):
                black_pegs += 1
                self.markPegsUsed(guess_peg_index, guess_peg_index)

        self.result['black pegs'] = black_pegs

    def checkPegsMatched(self, guess_peg_index, solution_peg_index):       
        return self.guess['pegs'][guess_peg_index] == self.solution['pegs'][solution_peg_index]

    def markPegsUsed(self, guess_peg_index, solution_peg_index):
        self.guess['pegIsUsed'][guess_peg_index] = True
        self.solution['pegIsUsed'][solution_peg_index] = True

    def updateWhiteResultPegsAndUsedPegs(self):
        white_pegs = 0
        
        for guess_peg_index in range(4):
            if self.guess['pegIsUsed'][guess_peg_index] == False:
                white_found, solution_peg_index = self.evaluateWhiteResultForSingleGuessPeg(guess_peg_index)
                white_pegs += white_found

                if solution_peg_index is not None:
                    self.markPegsUsed(guess_peg_index, solution_peg_index)
                    
        self.result['white pegs'] = white_pegs

    def evaluateWhiteResultForSingleGuessPeg(self, guess_peg_index):
        returnVal = (0,)
        for solution_peg_index in range(4):
            if self.checkIsWhite(guess_peg_index, solution_peg_index):
                returnVal = (1, solution_peg_index)

        if returnVal[0] == 1:
            return returnVal
        else:
            return (0, None)

    def checkIsWhite(self, guess_peg_index, solution_peg_index):
        white_candidate = self.checkWhiteCandidate(guess_peg_index, solution_peg_index)
        pegs_matched = self.checkPegsMatched(guess_peg_index, solution_peg_index)

        return white_candidate and pegs_matched

    def checkWhiteCandidate(self, guess_peg_index, solution_peg_index):
        return (solution_peg_index != guess_peg_index) and (self.solution['pegIsUsed'][solution_peg_index] == False)

    def printResult(self):
        black = self.result['black pegs']
        white = self.result['white pegs']
        plurality = {1 : '', 0 : 's', 1 : 's', 2: 's', 3 : 's', 4 : 's'}
        print('You recieved {} Black Peg{} and {} White Peg{}'.format(black, plurality[black], white, plurality[white]))
        

    def evaluateGameOver(self):
        if self.result['black pegs'] == 4:
            game_over = True
            win = True
        elif self.current_guess_number > self.max_guesses:
            game_over = True
            win = False
        else:
            game_over = False
            win = False

        return (game_over, win)



if __name__ == '__main__':
    solution = ('black','red','blue','green')

    guess1 = ('yellow','space','white','space')
    result1 = {'black pegs' : 0, 'white pegs' : 0}

    guess2 = ('yellow','black','white','space')
    result2 = {'black pegs' : 0, 'white pegs' : 1}

    guess3 = ('yellow','black','red','white')
    result3 = {'black pegs' : 0, 'white pegs' : 2}

    guess4 = ('red','blue','black','yellow')
    result4 = {'black pegs' : 0, 'white pegs' : 3}

    guess5 = ('blue','green','red','black')
    result5 = {'black pegs' : 0, 'white pegs' : 4}

    guess6 = ('green','white','yellow','green')
    result6 = {'black pegs' : 1, 'white pegs' : 0}

    guess7 = ('black','yellow','space','red')
    result7 = {'black pegs' : 1, 'white pegs' : 1}

    guess8 = ('space','blue','black','green')
    result8 = {'black pegs' : 1, 'white pegs' : 2}

    guess9 = ('green','black','blue','red')
    result9 = {'black pegs' : 1, 'white pegs' : 3}

    guess10 = ('red','red','white','green')
    result10 = {'black pegs' : 2, 'white pegs' : 0}

    guess11 = ('black','blue','black','green')
    result11 = {'black pegs' : 2, 'white pegs' : 1}

    guess12 = ('red','black','blue','green')
    result12 = {'black pegs' : 2, 'white pegs' : 2}

    guess13 = ('white','red','blue','green')
    result13 = {'black pegs' : 3, 'white pegs' : 0}

    guess14 = ('black','red','blue','green')
    result14 = {'black pegs' : 4, 'white pegs' : 0}
    
    game = MastermindGameState(solution)

    game.newGuess(guess1)
    game.assignResultPegs()
    assert game.result == result1

    game.prepareForNewGuess()
    game.newGuess(guess2)
    game.assignResultPegs()
    assert game.result == result2

    game.prepareForNewGuess()
    game.newGuess(guess3)
    game.assignResultPegs()
    assert game.result == result3
    
    game.prepareForNewGuess()
    game.newGuess(guess4)
    game.assignResultPegs()
    assert game.result == result4

    game.prepareForNewGuess()
    game.newGuess(guess5)
    game.assignResultPegs()
    assert game.result == result5
    
    game.prepareForNewGuess()
    game.newGuess(guess6)
    game.assignResultPegs()
    assert game.result == result6

    game.prepareForNewGuess()
    game.newGuess(guess7)
    game.assignResultPegs()
    assert game.result == result7    
    
    game.prepareForNewGuess()
    game.newGuess(guess8)
    game.assignResultPegs()
    assert game.result == result8

    game.prepareForNewGuess()
    game.newGuess(guess9)
    game.assignResultPegs()
    assert game.result == result9
    
    game.prepareForNewGuess()
    game.newGuess(guess10)
    game.assignResultPegs()
    assert game.result == result10

    game.prepareForNewGuess()
    game.newGuess(guess11)
    game.assignResultPegs()
    assert game.result == result11
    
    game.prepareForNewGuess()
    game.newGuess(guess12)
    game.assignResultPegs()
    assert game.result == result12

    game.prepareForNewGuess()
    game.newGuess(guess13)
    game.assignResultPegs()
    assert game.result == result13    
    
    game.prepareForNewGuess()
    game.newGuess(guess14)
    game.assignResultPegs()
    assert game.result == result14

    game.prepareForNewGuess()

    print('The solution was ', game.solution['pegs'])
    for i in range(1,15):
        print('Guess {} was'.format(i), game.history['guess{}'.format(i)], 'and the result was', game.history['result{}'.format(i)])
    























    
    



        
