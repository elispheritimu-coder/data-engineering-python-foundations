#create flags (print messages for users)
#x<18 on premium flag as minor 
#x>65 on free recomend senior plan
#total flagged minors &recomended seniors


users = [
    (12, "premium"),
    (70, "free"),
    (45, "premium"),
    (15, "premium"),
    (67, "free"),
    (30, "free"),
    (16, "free"),
    (10, "premium"),
    (80, "premium"),
]

flagged_minors = 0
upgrade_rec = 0

for age, account_type in users:
    if age < 18 and account_type == "premium":
         flagged_minors += 1
         print("premium is for adults", age)
    elif age > 65 and account_type == "free":
          upgrade_rec += 1
          print("upgrade to a senoir plan", age)

print ("n|summary")
print("total flagged minors", flagged_minors)
print("totol senior upgrade", upgrade_rec)
print("total flagged and upgrade recomendations:", flagged_minors + upgrade_rec)