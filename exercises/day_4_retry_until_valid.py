# Day 4 – retry until valid input
print("Script started")

while True:
    raw = input("Enter your age: ")

    try:
        age = int(raw)
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

print("You entered:", age)

if age >= 18:
    print("Access granted.")
else:
    print("Access denied.")
