import random
import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)

COLORS = [Fore.GREEN, Fore.RED, Fore.WHITE, Fore.YELLOW]

words = open('/usr/share/dict/words', 'r')
newWords = []

for word in words:
    if len(word) == 6:
        newWords.append(word.strip())

words.close()

chosen_word = random.choice(newWords).lower()

max_guesses = 5

guessed_words = []
print("Let's play wordle!")
print("Guess a five letter word")
display_word = '_' * len(chosen_word)
print(display_word)


print(chosen_word)
for i in range(max_guesses):
    # Get a word guess from the user
    guess = input('Guess a five letter word: ').lower()

    if len(guess) != 5:
        print('Please enter a five letter word')
        continue

    guessed_words.append(guess)

    display_word = ''.join(
        [letter if letter in guessed_words[-1] else '_' for letter in chosen_word])

    for j, letter in enumerate(display_word):
        if letter in guessed_words[-1]:
            if j == guessed_words[-1].index(letter):
                print(Back.GREEN + letter + Style.RESET_ALL, end=' ')
            else:
                print(Back.YELLOW + letter + Style.RESET_ALL, end=' ')
        else:
            print('_', end=' ')
    print()

    if guessed_words[-1] == chosen_word:
        print('You win!')
        break
    else:
        print('Incorrect.')

if guessed_words[-1] != chosen_word:
    print('You lose. The word was:', chosen_word)
