#day 6 filtering inside loops using the if statement

ages =[18, 22, 15, 30, 27]

adult_total =0
adult_count =0

for age in ages:
    if age >= 18:
        adult_total =adult_total + age
        adult_count =adult_count + 1 
print("total adult age:", adult_total)
print("number of adults:", adult_count)


#practice
ages = [18,22,27,15,30]
adult_count = 0

for age in ages:
    print("checking age:",age)
    if age >=18:
        adult_count += 1
    print("adult count so far:", adult_count)
