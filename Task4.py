import random
secret_number = random.randint(1, 20)
attempts = 524
print(" Guess the number between 1 and 20!")
print(f"You have {attempts} attempts.\n")
for i in range(attempts):
    guess = input(f"Attempt {i+1}: Enter your guess: ")
    if not guess.isdigit():
        print("Invalid input. Please enter a number.\n")
        continue
    guess = int(guess)
    if guess == secret_number:
        print(" Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low!\n")
    else:
        print("Too high!\n")
else:
    print(f" You've used all attempts. The number was {secret_number}.")