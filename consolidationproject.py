import os
import random

def word_selection(): # random word selection
    word_bank = ["horror", "romance", "action", "comedy"]
    return random.choice(word_bank)

def erase_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def letter_count(word, letter):
    count = word.count(letter)
    return count

erase_screen() 
print("Welcome to Bryant's Word Guessing Game, this is a single-player game. The theme of this word is movie genres.")
print("For the people who want to win, you may guess a letter. You can guess the entire word as well, although you only get three word guesses.")

word = word_selection()
print(f"The word this time is {word}")
guessed_letters = []
word_guesses = 0 
letter_guesses = 0
max_guesses = 3

while True:        
    display = ""
    for char in word:
        if char in guessed_letters:
            display += char
        else:
            display += "_"
    print("Guesses:", ", ".join(guessed_letters))
    print("Word guesses left:", max_guesses - word_guesses)
    guess = input("Choose wisely: ").lower()
    occurences = letter_count(word, guess)
    print(f"{guess} is seen in this word {occurences} times.")
    
    if (guess.isalpha() and len(guess) == 1) or (guess.isalpha() and len(guess) == len(word)):
        letter_guesses += 1
        if guess in guessed_letters:  # error troubleshooting
            print("Already used that letter.")
        else:
            guessed_letters.append(guess)
    if guess == word: # winning answer
        word_guesses += 1
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        print("Invalid guess. Please enter a single letter or a word.")

    if set(guessed_letters) == set(word):
        print("Congratulations! You guessed all the letters. The word was: '{}'.".format(word))
        break

    word_guesses += 1 #word guess counter
    if word_guesses >= max_guesses:
        print("You've reached the maximum number of word guesses. The word was: '{}'.".format(word))
        break