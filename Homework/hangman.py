import random

word_list = ["caden", "kansas", "ligma", "cheese", "python", "kangaroo", "burger", "germany","hollister","audition"]

def almighty_word():
    return random.choice(word_list)

def current_word_state(word, letters_guessed):
    word_display = ""
    for i in word:
        if i in letters_guessed:
            word_display += i
        else:
            word_display += "_"
    return word_display

def game():
    max_attempts = 20
    word = almighty_word()
    guessed_letters = []
    attempts = 0
    
    while True:
        print("Attempts:", max_attempts - attempts)
        display = current_word_state(word, guessed_letters)
        print(display)

        if display == word:
            print("You cheated ngl but you got it, it was: " + word)

        if attempts >= max_attempts:
            print("WRONG you suck, the word was: " + word)

        guess = input("Guess letter: ")

        guessed_letters.append(guess)

        if guess not in word:
            attempts += 1
            print("WRONG L bozo.")
    
game()
