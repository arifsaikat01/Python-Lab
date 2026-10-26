
def calculate_average(marks):
    if len(marks) == 0:
        return None

    total = sum(marks)
    average = total / len(marks)
    return average


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    if len(students) == 0:
        print("No student records available.")
        return

    for s in students:
        student_id = s[0]
        name = s[1]
        marks = s[2]

        print("Student ID:", student_id)
        print("Name:", name)

        
        if len(marks) == 0:
            print("No marks available.")
            print()
            continue

        
        valid = True

        for mark in marks:
            if mark < 0 or mark > 100:
                valid = False

        if valid == False:
            print("Invalid marks. Marks must be between 0 and 100.")
            print()
            continue

        average = calculate_average(marks)
        performance = classify_performance(average)

        print("Marks:", marks)
        print("Average:", round(average, 2))
        print("Performance:", performance)
        print()


students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],
    [206, "Karim", [75, 75, 75]],
    [207, "Mina", []],
    [208, "Rafi", [90, 105, 80]]
]

display_report(students)
