def greet():
    print("Welcome, Queen Ellie! madam Multi-millionaire")

# Calling the function
greet()
#parameters and arguments 
def greet(name):
    print(f"Welcome, {name}! This function now accepts parameters.")

greet("Ellie")
greet("Amina")
greet("David")

#return Vs Print 
def add_numbers(a, b):
     print (a + b)

result = add_numbers(5, 3)
print(result)
# return example 
def add_numbers(a, b):
     return a + b
#this gives the out put and hold the position 
result = add_numbers(5, 3)
print(result)

#return 
def calculate_total(numbers):
    total = sum(numbers)
    return (total)

ages = [25, 30, 45, 60] 

total_age = calculate_total(ages) 

print("Total age:", total_age)