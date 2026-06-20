def analyze_result(name, roll, marks):
    total = sum(marks)
    average = total / 5

    print("Student:", name, "(Roll:", roll, ")")
    print("Total:", total, "Average:", average)

    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 60:
        print("Grade: C")
    elif average >= 40:
        print("Grade: D")
    else:
        print("Fail")

    print("Subjects below 40:")
    for i in range(5):
        if marks[i] < 40:
            print("Subject", i + 1)

name = "Aarav"
roll = 101
marks = [88.5, 35.0, 76.0, 92.5, 48.0]

analyze_result(name, roll, marks)