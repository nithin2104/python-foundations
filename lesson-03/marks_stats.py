while True:
    try:
        num_students = int(input("Enter No of Students : "))
    except ValueError:
        print("Enter a valid number at least 1")
        continue
    else:
        if num_students < 1:
            print("Enter a valid number at least 1")
            continue
    students_marks = []
    passed_students_count = 0
    for i in range(num_students):
        while True:
            try:
                marks = int(input(f"Enter Student {i + 1} marks : "))
            except ValueError:
                print("Enter Whole numbers only")
            else:
                if marks < 0 or marks > 100:
                    print("Enter valid marks between 0 to 100")
                    continue
                else:
                    break
        students_marks.append(marks)

        if marks >= 40:
            passed_students_count += 1

    print(f"No of Students is = {len(students_marks)}")
    print(f"Highest Marks is = {max(students_marks)}")
    print(f"Lowest Marks is = {min(students_marks)}")
    print(f"Average Marks is = {sum(students_marks)/len(students_marks):,.2f}")
    print(f"Passed students count is = {passed_students_count}")
    break

