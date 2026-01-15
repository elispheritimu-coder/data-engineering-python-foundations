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

Total = 0

for age in ages:
    Total = Total + age 

print("Total age:", Total)
print("average age:", Total / len(ages))

