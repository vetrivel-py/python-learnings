print("Welcome to the number guessing game!!!")
print("Guess a number between 1 and 100")

encrypted_number = 63

while True:
    guessed_number = int(input("Enter your number: "))
    if guessed_number < 1 or guessed_number > 100:
        print("Please enter a number between 1 and 100")
    elif guessed_number < encrypted_number:
        print("Too low, try again")
    elif guessed_number > encrypted_number:
        print("Too high, try again")
    else:
        print("congratulations, you guessed the correct number!!!")
        break
