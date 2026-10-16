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
    if guess > 42:
        print("Too High")
    elif guess < 42:
        print("Too Low")
    else:
        if curr_try == 1:
            print(f"Correct! You Won. You guessed it in {curr_try} try.")
        else:
            print(f"Correct! You Won. You guessed it in {curr_try} tries.")

        break
if curr_try > MAX_TRIES:
    print("Out of tries")
