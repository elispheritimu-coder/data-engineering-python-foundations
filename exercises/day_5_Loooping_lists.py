  #day 5- looping througha list 
  
ages = [18, 22, 15, 30]

for age in ages:
  print("Age:", age)

#lists basics 

Ages = [18, 22, 15, 30]

print("all ages:", Ages)
print("first age:", Ages[0])
print("second age:", Ages[1])
print("last age:", Ages[-1])

#lists + conditions 

ages= [18, 22,25,30]

for age in ages:
    if age >= 18:
        print(age, "is an adult")
    else:
        print(age, "is a minor")
        