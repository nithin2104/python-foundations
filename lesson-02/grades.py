while True:
    try:
        marks = int(input("Enter marks : "))
    except ValueError:
        print("Please Enter a number between 0 to 100")
        continue
    else:
        if marks < 0 or marks > 100:
            print("Invalid Marks")
            print("Please Enter a number between 0 to 100")
            continue
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 60:
        print("C")
    elif marks >= 40:
        print("D")
    else:
        print("F")
    break
