marks = [
    [85, 90, 80],   
    [78, 88, 84],   
    [92, 76, 89]    
]
for i in range(3):
    total = sum(marks[i])
    average = total / len(marks[i])
    print(f"Student {i + 1} => Total: {total}, Average: {average:.2f}")