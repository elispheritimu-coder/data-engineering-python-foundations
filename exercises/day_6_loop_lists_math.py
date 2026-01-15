# inthe lists of ages find average teen age but only for even number age.

ages = [18, 22, 15, 30, 27, 14, 8, 9, 12, 17, 16, 13, 5, 7, 20, 19]
# counters and totals 

even_count_teen = 0
even_total_teen = 0

for age in ages:
    if 13 <= age <= 19: #teen range
        if age % 2 == 0: # if age is an even number
         print("even teen found:", age)
         even_count_teen = even_count_teen + 1
         even_total_teen = even_total_teen + age

    #the above gives us the total number of eve teen numbers and total age of even teen ages
    # the below now is to find the average but only if there are even numbers present.

if even_count_teen > 0:
    print("average even teen age", even_total_teen / even_count_teen)
else:
    print("no even teen age found :")
     