# filtering lists with conditional logic .
#Filter a list of ages and find the total and average age of minors (under 18).


ages = [18, 22, 15, 30, 27, 12, 17, 8]

minor_total = 0
minor_count = 0

for age in ages:
    
    if age < 18:
        print("minor found:", age)
        minor_total = minor_total + age
        minor_count = minor_count + 1
        print("minor count so far:", minor_count)
    
    if minor_count > 0:
        average_minor_age =minor_total / minor_count
        print("average_minor_age:", average_minor_age)
        print("total_minor_age:", minor_total)

    else:
        print("no minor found.")


# lists with multiple conditions (if, elif and else)
#goal :categorize pop into {children, teens(13-17) adults>18} &find total and average for each


ages = [12, 17, 22, 9, 14, 18, 30, 5, 16, 27]

#initialize counters and totals


count_children = 0
count_teen = 0
count_adult = 0

total_children = 0
total_teen = 0 
total_adult = 0

for age in ages:
    if age < 13:
        print("child found:", age)
        count_children = count_children + 1
        total_children =total_children + age
    elif 13 <= age >= 17:
        print("teen found:", age)
        count_teen = count_teen + 1
        total_teen = total_teen + age
    else:
        print("adult found:", age)
        count_adult =+ 1
        total_adult =+ age

#final summaries:
print("\n--- final countsn---")
print("print children", count_children, "average:",total_children /count_children if count_children else 0)
print("teens:", count_teen, "average",total_teen /count_teen if count_teen else 0)
print("adults:", total_adult, "average:", total_adult / total_adult if total_adult else 0)