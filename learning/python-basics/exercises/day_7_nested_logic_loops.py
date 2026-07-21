# nested logic with conditions inside a loop
#identify adults and among them tag seniors if the are 60+
#to keep the logic keen and avoid duplicate runs/checks 

ages = [5, 12, 17, 18, 22, 30, 65, 70, 11, 13, 16, 64]

for age in ages:
    if age >= 18:
        category = "adult"
        if age >= 60:
            subcategory = "senior"
        else:
            subcategory = "young adults"

    else:
        category = "minor"
        if age < 13:
            subcategory = "child"
        else:
            subcategory = "teen"
print("age:", age, "|main category:", category, "|subcategory:", subcategory)

#nested logic line by line 
#2nd decision depends on 1st 
ages = [12, 25, 70]

for age in ages:
    if age >= 18:
        print("Adult logic:", age)
        if age >= 60:
            print(" → Senior:", age)
        else:
            print(" → Young adult:", age)
    else:
        print("Minor logic:", age)
        if age < 13:
            print(" → Child:", age)
        else:
            print(" → Teen:", age)


#nested logic practice - Grouping logic by category
#You're analyzing a shopping cart.
    #If the cart total is over $100, you want to apply premium rules.
    #Inside that block, if the customer is a VIP, they get an extra discount.
    #If the cart total is below $100, they only get standard offers.

cart_total = 90
is_vip = False

if cart_total >= 100:
      print ("apply premium rules.")
      if is_vip:
        print("Vip customer: apply 20% discount")
      else:
        print("regular customer: apply 10% discount.")
else:
    print("standard pricing rules")
    print("no special discount")



    # Day 7 - Nested logic inside a loop

scores = [95, 82, 67, 45, 89, 100, 73, 38, 91]

for score in scores:
    if score >= 50:
        print("Score:", score, "| Result: PASS")
        
        if score >= 90:
            print(" → Honors student")
        else:
            print(" → Regular pass")

    else:
        print("Score:", score, "| Result: FAIL")
