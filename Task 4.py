# All students in class
all_students = {"Akanksha", "Arpita", "Dipu", "Chirag", "Manya", "Kritika", "Ayush", "Sneha", "Rohan", "Palak"}

# Students who play football
football = {"Akanksha", "Chirag", "Ayush", "Rohan", "Sneha"}

# Students who play cricket
cricket = {"Arpita", "Chirag", "Dipu", "Sneha", "Palak"}

# Students who play both
both = football & cricket
print("🟢 Students who play BOTH football and cricket:")
print(both)

# Students who play only one
only_one = football ^ cricket
print("\n🟡 Students who play ONLY ONE game:")
print(only_one)

# Students who play none
none = all_students - (football | cricket)
print("\n🔴 Students who play NONE:")
print(none)
