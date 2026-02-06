import csv

valid_users = []
invalid_users = []

# Step 1: Read users from CSV
with open("raw_user.csv", "r") as file:
    reader = csv.DictReader(file)
    raw_data = list(reader)

# Step 2: Validate and classify users
for user in raw_data:
    name = user.get("name", "").strip()
    email = user.get("email", "").strip()

    # Clean fields
    user["name"] = name
    user["email"] = email

    # Validation rules
    if not name:
        user["reason"] = "Missing name"
        invalid_users.append(user)
    elif not email:
        user["reason"] = "Missing email"
        invalid_users.append(user)
    elif "@" not in email or "." not in email:
        user["reason"] = "Invalid email format"
        invalid_users.append(user)
    else:
        valid_users.append(user)

# Step 3: Save valid users
with open("clean_users_b5.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "email"])
    writer.writeheader()
    writer.writerows(valid_users)

# Step 4: Save invalid users with reason
with open("invalid_users_b5.txt", "w") as file:
    for user in invalid_users:
        file.write(f"{user['name'] or 'N/A'} | {user['email'] or 'N/A'} | Reason: {user['reason']}\n")

# Step 5: Summary report
total = len(raw_data)
valid = len(valid_users)
invalid = len(invalid_users)
valid_pct = (valid / total) * 100 if total else 0
invalid_pct = 100 - valid_pct

print("\n📊 Summary Report")
print(f"Total: {total}")
print(f" Valid: {valid} ({valid_pct:.1f}%)")
print(f" Invalid: {invalid} ({invalid_pct:.1f}%)")