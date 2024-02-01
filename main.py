import getpass


class Hangman:

  def __init__(self) -> None:
    self._guessedFails = []
    self._guessedSuccess = []
    self._searchWord = ""

  def startGame(self):
    self._searchWord = getpass.getpass("Enter a word for the other player to guess: ").lower()
    while len(self._searchWord.split(" ")) > 1 or len(self._searchWord) == 0:
      print("Input needs to be one word!")
      self._searchWord = getpass.getpass("Enter a word for the other player to guess: ").lower()
    else:
      print("Word saved successfully!\n")

      while self._gameRunning():
        print(
            f"Guess progress: {self._getGuessed()}\nFails: {len(self._guessedFails)}/10\n"
        )
        self._doGuess()

  def _gameRunning(self) -> bool:
    if (len(self._guessedFails) >= 10):
      print(
          f"Too many fails: You lost!\nThe word was {self._searchWord}"
      )
      return False
    elif self._getGuessed() == self._searchWord:
      print(f"You guessed the word successfully. It was {self._searchWord}")
      return False
    else:
      return True

  def _getGuessed(self) -> str:
    guessString = ""
    for x in self._searchWord:
      if x in self._guessedSuccess:
        guessString += x
      else:
        guessString += "_"
    return guessString

  def _doGuess(self):
    guess = input("Guess a character: ").lower()
    while len(guess) > 1:
      print("Invalid input, please enter a single character!")
      guess = input("Guess a character: ").lower()
    if guess in self._guessedFails or guess in self._guessedSuccess:
      print("You already guessed this character!")
    else:
      if guess in self._searchWord:
        self._guessedSuccess.append(guess)
      else:
        self._guessedFails.append(guess)


game = Hangman()
game.startGame()
