#Categorize by age group (child, teen, adult, senior)
#flag:minors on premium, senior on free, inacrive users (watch time < 2hrs)
#suggest upgrades.

#Dataset (age,account_type, hours_watched)
users = [
    (12, "premium", 1.5),
    (22, "free", 5.0),
    (67, "free", 1.0),
    (15, "premium", 0.5),
    (45, "premium", 6.0),
    (30, "free", 3.0),
    (13, "free", 1.0),
    (64, "premium", 0.0),
    (80, "free", 2.5),
    (17, "premium", 1.0)
]

flagged_minors = 0
upgrade_suggestions = 0
inactive_users = 0
total_users = 0

for age, account, hours in users:
    total_users += 1
    print(f"\nUser: Age {age}, Account: {account}, Hours watched: {hours}")
    
    # Categorize by age
    if age < 13:
        category = "child"
    elif age <= 17:
        category = "teen"
    elif age <= 65:
        category = "adult"
    else:
        category = "senior"
    
    print("Category:", category)

    # Now apply nested logic
    if age < 18 and account == "premium":
        flagged_minors += 1
        print("⚠️  Flagged: Minor on premium plan.")

    if age > 65 and account == "free":
        upgrade_suggestions += 1
        print("💡 Suggestion: Recommend senior upgrade.")

    if hours < 2:
        inactive_users += 1
        print("🛑 Inactive user detected.")

# Summary
print("\n=== Summary ===")
print("Total users:", total_users)
print("Flagged minors on premium:", flagged_minors)
print("Senior upgrade suggestions:", upgrade_suggestions)
print("Inactive users:", inactive_users)

      