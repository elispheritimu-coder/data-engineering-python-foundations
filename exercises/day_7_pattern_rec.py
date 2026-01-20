#categorize ages 

ages = [5, 12, 17, 18, 22, 30, 65, 70, 11, 13, 16, 64]

for age in ages:
    if age < 13:
        category = "child"
    elif age <= 17:
         category = "teen"
    elif age < 65:
         category = "adult"
    else:
        category = "senior"
    print("age:", age, "|category:", category)

# 2. Condition OUTSIDE loop
age = 5
if age < 13:
    for age in ages:
        print(age)
