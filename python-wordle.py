import random
import sys
from colorama import init, Fore, Back, Style
init(autoreset=True)

COLORS = [Fore.GREEN, Fore.RED, Fore.WHITE, Fore.YELLOW]

words = open('/usr/share/dict/words', 'r')
newWords = []

for word in words:
    if len(word) == 6:
        newWords.append(word)

word = random.choice(newWords).lower()

print("Lets play wordle:")
print("Type a 5 letter word and hit enter")


for attempt in range(1, 7):
    guess = input().lower()

    for i in range(min(len(guess), 5)):
        if guess[i] == word[i]:
            print(Fore.GREEN+(guess[i]), end="")

        elif guess[i] in word:
            print(Fore.YELLOW+(guess[i]), end="")
        else:
            print(guess[i], end="")

    if guess == word:
        print(Fore.GREEN(f"congrats! You guessed the wordle in {attempt}"))
    elif attempt == 6:
        print("You ran out of attempts. You lose")
