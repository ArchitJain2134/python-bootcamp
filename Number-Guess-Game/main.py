import random

print("Welcome to the Number Guessing Game")
random_number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100")
difficulty_level = input("Choose a Difficulty level. Type 'easy' or 'hard': ").lower()


if difficulty_level == 'easy':
    attempts_left = 10
elif difficulty_level == 'hard':
    attempts_left = 5


while attempts_left > 0:
    print(f"You have {attempts_left} attempts left")
    guess_number = int(input("Guess a number:  "))
    if guess_number < random_number:
        print(" Too Low \n Guess Again")
        attempts_left -= 1
    elif guess_number > random_number:
        print(" Too High \n Guess Again")
        attempts_left -= 1
    elif guess_number == random_number:
        print(" Congratulations! You guessed the number!")
        break
    else:
        print("Error")

