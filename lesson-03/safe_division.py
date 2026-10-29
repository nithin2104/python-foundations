while True:
    try:
        num1 = int(input("Enter number 1 : "))
        if num1 < 0:
            raise ValueError("Number can not be negative")
    except ValueError:
        print("Enter positive integers")
        continue
    else:
        break
while True:
    try:
        num2 = int(input("Enter number 2 : "))
        if num2 < 0:
            raise ValueError("Number can not be negative")
    except ValueError:
        print("Enter positive integers")
    else:
        break

try:
    answer = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Division can only be performed on numbers")
else:
    print(f"Division of {num1} / {num2} = {answer}.")
finally:
    print("Calculation Finished!")
