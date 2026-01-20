#analyzing a small list of users from a streaming service 
#each user has a watch time and account type (free, premium, vip)
#flag inactive premium/vip users<3hrs
#suggest upgrade to free users watching >10hrs
#tract total number of users processed

#dataset

users = [
    (2.5, "premium"),
    (12.0, "free"),
    (0.5, "vip"),
    (6.0, "free"),
    (15.0, "vip"),
    (1.5, "premium"),
    (10.5, "free"),
    (4.0, "vip"),
    (3.0, "premium"),
]

inactive_vip = 0
inactive_premium = 0
upgrade_suggestions = 0
total_users = 0

for hour, account_type in users:
    total_users += 1
    if hour < 3 and account_type == "vip":
        inactive_vip = inactive_vip + 1
    if hour > 10 and account_type == "free":
        upgrade_suggestions += 1
    if hour < 3 and account_type == "premium":
        inactive_premium = inactive_premium + 1
print("n|summary")
print("inactive users:", inactive_vip)
print("inactive users:",inactive_premium)
print("total inactive users:",inactive_vip + inactive_premium)
print("upgrade sugestions:", upgrade_suggestions)
print("total users:", total_users)

