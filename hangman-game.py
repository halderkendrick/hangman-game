import random

def hangman():
    word_list = ["python", "programming", "hangman", "development", "challenge"]
    word_to_guess = random.choice(word_list)
    guessed_letters = []
    attempts_remaining = 6

    print("Welcome to Hangman!")
    print("_ " * len(word_to_guess))

    while attempts_remaining > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts_remaining -= 1
            print(f"Sorry, '{guess}' is not in the word. Attempts remaining: {attempts_remaining}")

        current_progress = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print("Current progress: ", ' '.join(current_progress))

        if '_' not in current_progress:
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"Game over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
