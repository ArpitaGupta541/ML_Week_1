students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}
def search_student(roll):
    if roll in students:
        print(f"Roll Number {roll} belongs to: {students[roll]}")
    else:
        print(f"Roll Number {roll} not found.")
search_student(102)   
search_student(105)   