MAX_TRIES = 5
SECRET_NUMBER = 42
curr_try = 0
while curr_try < MAX_TRIES:
    while True:
        try:
            guess = int(input("Guess the number : "))
        except ValueError:
            print("Enter Whole numbers only")
        else:
            break
    curr_try += 1
    if guess > SECRET_NUMBER:
        print("Too High")
    elif guess < SECRET_NUMBER:
        print("Too Low")
    else:
        if curr_try == 1:
            print(f"Correct! You Won. You guessed it in {curr_try} try.")
        else:
            print(f"Correct! You Won. You guessed it in {curr_try} tries.")
        break
else:
    print("Out of tries")
