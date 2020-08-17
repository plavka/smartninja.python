secret = 13
guess = int(input("Guess the secret number (between 1 and 20)"))
if guess == secret:
    print("You're right, secret number is 13. Congrats.")
else:
    print("Sorry, you're wrong. Guess again.")