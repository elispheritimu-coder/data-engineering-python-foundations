# Royal Data Purge Script - 10 Day Challenge Recap

import csv

# Step 1: Load raw user data
royal_raw_users = []
with open("royal_raw_users.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        royal_raw_users.append(row)

# Step 2: Clean and validate
royal_clean_users = []
royal_invalid_users = []

for user in royal_raw_users:
    name = user.get("name", "").strip()
    email = user.get("email", "").strip().lower()
    country = user.get("country", "").strip().title()

    # Start validation
    if not name or not email:
        user["error"] = "Missing name or email"
        royal_invalid_users.append(user)
    elif "@" not in email or "." not in email:
        user["error"] = "Invalid email format"
        royal_invalid_users.append(user)
    elif country == "":
        user["error"] = "Missing country"
        royal_invalid_users.append(user)
    else:
        royal_clean_users.append({
            "name": name,
            "email": email,
            "country": country
        })

# Step 3: Write clean users to CSV
with open("royal_clean_users.csv", mode="w", newline="") as file:
    fieldnames = ["name", "email", "country"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for user in royal_clean_users:
        writer.writerow(user)

# Step 4: Write invalid users and their errors to TXT
with open("royal_invalid_users.txt", mode="w") as file:
    for user in royal_invalid_users:
        file.write(f"Name: {user.get('name', 'N/A')}, "
                   f"Email: {user.get('email', 'N/A')}, "
                   f"Country: {user.get('country', 'N/A')}, "
                   f"Error: {user['error']}\n")

# Step 5: Royal Summary
print("\n Data Purge Report ")
print(f"Total royal records reviewed: {len(royal_raw_users)}")
print(f"✅ Royal Clean users: {len(royal_clean_users)}")
print(f"❌  Royal Invalid users: {len(royal_invalid_users)}")