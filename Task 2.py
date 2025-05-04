students = [
    (101, "Alice", 20),
    (102, "Bob", 21),
    (103, "Charlie", 19)
]
print("Student Information:\n")
print("Roll No\tName\t\tAge")
print("---------------------------")
for student in students:
    roll, name, age = student
    print(f"{roll}\t{name}\t\t{age}")