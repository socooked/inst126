import os
import random

def word_selection():
        word_bank = ["horror", "romance", "action", "comedy"]
        return random.choice(word_bank)

def erase_screen(): #easier to read code if u clear the screen
       os.system('cls' if os.name == 'nt' else 'clear') 
    
def letter_count(word, letter):
    count = 0 
    for char in word: 
         if char == letter:
              count += 1
              return count

class start_game():    
    word = word_selection()
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
                    display += ""
                    
            print(f"Welcome to Bryant's Word Guessing Game, this is a single-player game. The theme of this word is movie genres.")
            print("Guessed letters:", ", ".join(guessed_letters))
            print ("Word guesses left:", max_guesses - word_guesses)

            guess = input ("For the people who want to win, you may guess a letter. You can guess the entire word as well, although you only get three word guesses. Choose wisely.").lower()

            if (guess.isalpha() and len(guess) == 1) or (guess.isalpha() and len(guess) == len(word)):
                letter_guesses += 1
                if guess in guessed_letters:
                    print("Already used that letter dummy.")
                else:
                    guessed_letters.append(guess)
                    occurences = letter_count(word, guess)
                print("{} is seen in this word {} times.".format(occurences,guess))
                if set(guessed_letters) == set(word):
                        print("wow...you won. Only took {} tries...".format(letter_guesses))
                        break
            else:
                print("Nah yo. Input only a word or singular letter.")

            if len(guess) == len(word) and guess.isalpha():
                word_guesses += 1
                if guess == word:
                    print("Nice,only took {} tries to guess the word.".format(letter_guesses))
                    break        
            else:
                print("Wrong word dummy.")
            if word_guesses == 3:
                print("Ya lost twin. Outta guesses...")
                break
     
if __name__ == "__main__":
    start_game
