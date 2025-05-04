temperatures = []
for i in range(1, 6):
    temp = float(input(f"Enter temperature for Day {i}: "))
    temperatures.append(temp)
average_temp = sum(temperatures) / len(temperatures)
print("\nTemperatures entered:", temperatures)
print(f"Average temperature over 5 days: {average_temp:.2f}°C")
