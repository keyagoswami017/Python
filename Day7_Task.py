import random

# Select the random word
print("Word to guess")
word_list = ['rock','paper','scissors','mouse','apple']
word_selected = random.choice(word_list)

# Create a placeholder for the word to show dashes
placeholder = ""
for i in range(len(word_selected)):
    placeholder +="_"
print("Total Letters in word ",placeholder)

# To check the letter
correct_letters = []
lives = 6
game_over = False
while not game_over:
        print(f"{lives} / 6 lives are left for you")
        guess = input("Guess a letter\n").lower()
        if guess in correct_letters:
            print(f"You've already guessed this letter {guess}")

        display = ""
        for letter in word_selected:
                if letter == guess:
                    display += letter
                    correct_letters.append(letter)
                elif letter in correct_letters:
                     display += letter
                else:
                    display += "_"

        print(display)
        if guess not in word_selected:
            print(f"You guessed this letter {guess} which is not in the word ")
            lives -= 1

            print("Your remaining life is ", lives)
            if lives == 0:
                game_over = True
                print("\nLives Over......... You Lose!")

        if "_" not in display:
            print("You win!")
            game_over = True
