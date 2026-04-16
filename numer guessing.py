import random

number = random.randint(1, 100)
attempts = 5

print("Guess a number between 1 and 100")

for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You win!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")

    print("Attempts left:", attempts - i - 1)

else:
    print("😢 You lost! The number was:", number)