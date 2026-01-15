# day 6 basic statistics on a list

ages = [18, 22, 25, 30, 27]

print("Ages:",ages)
print("Number of recods:", len(ages))
print("minimum age:", min(ages))
print('maximum age:', max(ages))
print("total;",sum(ages))
print(sum(ages)/len(ages), ("average age"))


#manual sum using a loop 

ages = [18, 22, 15, 30, 27]

total = 0

for age in ages:
    total = total + age 

print("total age:", total)
print("average age:", total / len(ages))

#test on range checking 
ages = [15, 18, 21, 25, 30, 12, 60, 61]

for age in ages:
    if 18<=age<=60:
        print(age ,"age:")
    if age % 2 == 0:
        print("even age found:", age)
    else:
            print("no even age found")
