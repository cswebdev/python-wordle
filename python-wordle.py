import random
import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)

COLORS = [Fore.GREEN, Fore.RED, Fore.WHITE, Fore.YELLOW]

words = open('/usr/share/dict/words', 'r')
newWords = []

for word in words:
    if len(word) == 6:
        newWords.append(word)

words.close()

chosen_word = random.choice(newWords).lower()

max_guesses = 5

guessed_letters = []
print("Lets play wordle!")
print("Guess a letter or a five letter word")
display_word = '_' * len(chosen_word)
print(display_word)

for i in range(max_guesses):
    # Get a letter guess from the user
    guess = input('Guess a letter: ')

    guessed_letters.append(guess)

    display_word = ''.join(
        [letter if letter in guessed_letters else '_' for letter in chosen_word])

    for letter in display_word:
        if letter == guess:
            print(colorama.Back.GREEN + letter +
                  colorama.Style.RESET_ALL, end=' ')
        else:
            print(letter, end=' ')
    print()

    if guess in chosen_word:
        print('Correct!')
    else:
        print('Incorrect.')

    if display_word == chosen_word:
        print('You win!')
        break
else:
    print('You lose. The word was:', chosen_word)
