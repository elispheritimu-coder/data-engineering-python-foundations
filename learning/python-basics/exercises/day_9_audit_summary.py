#generate a final audit summurry showing 
  #total users processsed 
  #total were clean
  #total flagged
  #percentage breakdown


users = [
    {"name": "Alice", "email": "alice@gmail.com"},
    {"name": "bob123", "email": "bob_at_gmail.com"},
    {"name": "CHARLIE", "email": "charlie@yahoo.org"},
    {"name": "daisy$", "email": "daisy@yahoo"},
    {"name": "eve", "email": "test@unknown.com"},
    {"name": "frank", "email": "   FRANK@outlook.net   "},
    {"name": "gina", "email": "no_email"},
]
# Sample setup  the counters
total_users = len(users)
clean_users = []
flagged_users = []

banned_emails = ["no_email", "test@unknown.com"]
valid_domains = [".com", ".org", ".net"]

for user in users:
    name = user.get("name", "").strip().title() #correcting the space and capitalize
    email = user.get("email", "").strip().lower()# corecting space and lower case 
    
    name_valid = name.isalpha()#validating name 
    email_valid = (
        "@" in email and 
        email.endswith(tuple(valid_domains)) and     #validating email
        email not in banned_emails
    )

    if name_valid and email_valid:
        clean_users.append(user)   #summing up 
    else:
        flagged_users.append(user)

# Final Summary
print("\n🧾 AUDIT SUMMARY")
print(f"Total users checked: {total_users}")
print(f" Clean users: {len(clean_users)}")
print(f" Flagged users: {len(flagged_users)}")

# Bonus: Percentage calculations
clean_pct = (len(clean_users) / total_users) * 100
flagged_pct = (len(flagged_users) / total_users) * 100

print(f"\nBreakdown:")
print(f" Clean: {clean_pct:.1f}%")
print(f" Flagged: {flagged_pct:.1f}%")

print("\n👑 Clean Usernames:")
for user in clean_users:
    print(f"• {user['name']} ({user['email']})")


#saving the file to a .txt
with open("flagged_users.txt", "w") as file:
    file.write("Flagged Users Report\n\n")
    for user in flagged_users:
        name = user.get("name", "Unnamed")
        email = user.get("email", "No email")
        file.write(f"Username: {name}, Email: {email}\n")
#this creates a flie called flagged users.txt in my projrct folder (python-basics)

#saving the file as a .csv
import csv

with open("flagged_users.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Email"])  # Header

    for user in flagged_users:
        name = user.get("name", "Unnamed")
        email = user.get("email", "No email")
        writer.writerow([name, email])
#good for sharing,uploading or importing to power BI tools 
