marks = int(input("Enter marks : "))
if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 75 and marks <= 89:
    print("B")
elif marks >= 60 and marks <= 74:
    print("C")
elif marks >= 40 and marks <= 59:
    print("D")
elif marks < 40:
    print("F")
else:
    print("Invalid Marks")
