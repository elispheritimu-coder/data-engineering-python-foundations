# Day 3 - Safe decision making

try:
    age = int(input("Enter Your Age."))

    if age >= 18:
        print("Access granted. You are an adult.")
    else:
        print("Access denied. You are under 18.")

except ValueError:
    print("Invalid input. Please enter a number.")
