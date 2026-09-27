import random

# This is a number guessing game

def guess_num(attempts):
    num_found = False
    while not num_found and attempts > 0:
        print(f"You've {attempts} attempts lefts to guess the number\n")
        num = int(input("Make a guess\n"))
        if num < random_num:
            print("Too low")
            attempts = attempts - 1
        elif num > random_num:
            print("Too high")
            attempts = attempts - 1
        else:
            print(f"You guessed correctly {num}")
            num_found = True

    if num_found:
        print("You win!")
    else:
        print("You lose!")


print("Welcome to the number guessing game!!!")
print("I am thinking of a number between 1 and 100")
random_num = random.randint(1,101)
choice = input("choose difficulty. Type 'easy' or 'hard':\n")
EASY_ATTEMPT = 10
HARD_ATTEMPT = 5

if choice == "easy":
    guess_num(EASY_ATTEMPT)
elif choice == "hard":
    guess_num(HARD_ATTEMPT)
else:
    print("Invalid attempts and choice!!!")
