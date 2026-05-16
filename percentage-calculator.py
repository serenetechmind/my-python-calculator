# Percentage Calculator Program

# 1. Ask the user for the total number and the percentage they want to find
# We use float() so the user can type whole numbers or decimals
number = float(input("Enter the number: "))
percentage = float(input("Enter the percentage value (e.g., 15 for 15%): "))

result = (percentage_val / 100) * number

print(f"{percentage}% of {number} is: {result}")
