import getpass


class Hangman:

  def __init__(self) -> None:
    self._guessedFails = []
    self._guessedSuccess = []
    self._searchWord = ""

  def startGame(self):
    self._searchWord = getpass.getpass("Gib das zu erratene Wort ein: ")
    while len(self._searchWord.split(" ")) > 1 or len(self._searchWord) == 0:
      print("Das Wort muss ein Wort sein!")
      self._searchWord = getpass.getpass("Gib das zu erratene Wort ein: ")
    else:
      self._searchWord = self._searchWord.lower()
      print("Das Wort wurde erfolgreich eingegeben!\n")

      while self._gameRunning():
        print(
            f"Das Wort sieht so aus: {self._getGuessed()}\nFails: {len(self._guessedFails)}/10\n"
        )
        self._doGuess()

  def _gameRunning(self) -> bool:
    if (len(self._guessedFails) >= 10):
      print(
          f"Zu viele Fehler! Du hast verloren!\nDas Wort war {self._searchWord}"
      )
      return False
    elif self._getGuessed() == self._searchWord:
      print(f"Du hast das Wort erfolgreich erraten. Es war {self._searchWord}")
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
    guess = input("Rate einen Buchstaben: ").lower()
    while len(guess) > 1:
      print("Ungültige Eingabe, bitte gib nur einen Buchstaben ein!")
      guess = input("Rate einen Buchstaben: ")
    if guess in self._guessedFails or guess in self._guessedSuccess:
      print("Du hast diesen Buchstaben bereits geraten!")
    else:
      if guess in self._searchWord:
        self._guessedSuccess.append(guess)
      else:
        self._guessedFails.append(guess)


game = Hangman()
game.startGame()
