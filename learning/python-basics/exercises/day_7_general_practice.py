

ages = [21, 25, 27, 30]

print ("all ages:", ages)
print("first age:", ages[0])
print("last age:", ages[-1])

ages[1] = 26 #making value in index 1 to be 26 .
print("updated ages:", ages)
#logic inside loops 
next_year_ages = []


for age in ages:
    new_age = age + 1
    next_year_ages.append(new_age)
print("next_year_ages:", next_year_ages)
   
#lool n lists


ages = [15, 21, 25, 17, 30]
print("\nAge categories:")

for age in ages:
    if age < 18:
        print(age, "→ Minor")
    elif age <= 60:
        print(age, "→ Adult")
    else:
        print(age, "→ Senior")

#creating new lists after filreting 


ages = [15, 21, 25, 17, 30, 65]
minors = []
adults = []

for age in ages:
    if age < 18:
        minors.append(age)
    else:
        adults.append(age)
print("minors:", minors)
print("adults:", adults)




print("\nMini data pipeline:")

ages = [15, 21, 25, 17, 30, 65]

# Filter
adults = []
for age in ages:
    if age >= 18:
        adults.append(age)

# Transform
adults_next_year = []
for age in adults:
    adults_next_year.append(age + 1)

# Aggregate
count = len(adults_next_year)

total = 0
for age in adults_next_year:
    total += age

average = total / count

# Output
print("Raw ages:", ages)
print("Adults:", adults)
print("Adults next year:", adults_next_year)
print("Count:", count)
print("Average adult age:", average)
