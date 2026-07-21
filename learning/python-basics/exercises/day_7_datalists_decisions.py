#real data values to triger decisions 

  #a list of users :print a custom message based on age an account type 
  #if > 18 with a premimum account :warn its for adults only
  #if <= 18 with a free account :suggest an upgrade
  #otherwise just greet them normally .

  #Data :each user has (age, account_type)
# Data: each user has (age, account_type)
users = [
    (16, "premium"),
    (22, "free"),
    (17, "free"),
    (45, "premium"),
    (30, "free"),
    (13, "free"),
    (21, "premium")
]

for age, account in users:
    print("User Age:", age, "| Account:", account)

    if age < 18:
        if account == "premium":
            print(" → Warning: Premium is for adults only.")
        else:
            print(" → Welcome, young user.")
    else:
        if account == "free":
            print(" → Consider upgrading to premium.")
        else:
            print(" → Thank you for being a premium user.")


#How many users were flagged
#how many minors were on premium
#what is the number of upgrade suggestions 

users = [
    (16, "premium"),
    (22, "free"),
    (17, "free"),
    (45, "premium"),
    (30, "free"),
    (13, "free"),
    (21, "premium")
]

flagged_minors = 0
upgrade_suggestions = 0
total_users = 0

for age, account in users:
    total_users += 1

    if age < 18 and account == "premium":
        flagged_minors += 1
    elif age >= 18 and account == "free":
        upgrade_suggestions += 1

print("\n--- Summary ---")
print("Total users processed:", total_users)
print("Minors on premium (flagged):", flagged_minors)
print("Adults on free (suggest upgrade):", upgrade_suggestions)
