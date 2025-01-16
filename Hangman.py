import random

def hangman():
    words = ["python", "hangman", "code", "simple", "game"]
    selected_word = random.choice(words)
    guessed_word = ["_" for _ in selected_word]
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman! Let's play!")

    while attempts_left > 0 and "_" in guessed_word:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Attempts remaining: {attempts_left}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Oops! Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already tried that letter! Try something new.")
            continue

        guessed_letters.add(guess)

        if guess in selected_word:
            print("Nice! You found a letter.")
            for idx, letter in enumerate(selected_word):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print("Oops! That letter is not part of the word.")
            attempts_left -= 1

    if "_" not in guessed_word:
        print(f"\nCongratulations! You guessed the word: {selected_word}")
    else:
        print(f"\nGame over!The word was: {selected_word}. Try next time!")

if __name__ == "__main__":
    hangman()
