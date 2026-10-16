tries = 0
while True:
    if tries >= 5:
        print("Out of tries")
        break
    guess = int(input("Guess the number : "))
    tries += 1
    if guess > 42:
        print("Higher")
    elif guess < 42:
        print("Lower")
    else:
        print(f"Correct! You Won. You guessed it in {tries} tries.")
        break
