def guess_number():

    import random

    print("Welcome to the number guessing game!!!")
    print("Guess a number between 1 and 100")
    print("You have 7 attempts to guess the number correctly, good luck!!!")

    encrypted_number = random.randint(1, 100)

    for i in range(1, 8):
        try:   
            guessed_number = int(input("Enter your number: "))
            if guessed_number < 1 or guessed_number > 100:
                print("Please enter a number between 1 and 100")
            elif guessed_number < encrypted_number:
                print("Your number is lesser, try again")
            elif guessed_number > encrypted_number:
                print("Your number is higher, try again")
            else:
                print("your guessed number is correct!!!")
                break
        except ValueError:
            print("Invalid characters found, please enter a valid number between 1 and 100")
    if guessed_number == encrypted_number:
        print(f"Congratulations, you guessed the number {encrypted_number} in {i} attempts!!!")
    else:
        print(f"All limits are exceeded, Please try again !!! and the number was {encrypted_number}")

if __name__ == "__main__":
    guess_number()