# Grading System

marks = int(input("Enter your marks (0-100): "))
if marks < 0 or marks > 100:
    grade = "Invalid marks entered."
elif marks >= 90:
    grade = "Grade: A"
elif marks >= 75:
    grade = "Grade: B"
elif marks >= 60:
    grade = "Grade: C"
elif marks >= 40:
    grade = "Grade: D"
else:
    grade = "Fail"
print(grade)
