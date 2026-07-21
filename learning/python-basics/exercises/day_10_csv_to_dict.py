import csv #We import the csv module for saving clean data laterwe can move 

# Lists to store clean and invalid users
valid_users = []
invalid_users = []

# Open the CSV file
with open("raw_user.csv", "r") as file:
    lines = file.readlines()

# Check if file has any content
if not lines:
    print("File is empty. Nothing to process.")
else:
    header = lines[0].strip()
    data_lines = lines[1:]  # Skip header

    for line in data_lines:
        cleaned = line.strip()
        if not cleaned:
            continue  # skip empty lines

        parts = cleaned.split(",")
        if len(parts) != 2:
            print(f" Skipping malformed row: {cleaned}")
            invalid_users.append(cleaned)
            continue

        name, email = parts[0].strip(), parts[1].strip()

        # Email must have both '@' and '.'
        if "@" in email and "." in email:
            user_dict = {
                "name": name,
                "email": email
            }
            valid_users.append(user_dict)
        else:
            invalid_users.append(f"{name} → {email}")

# ✨ Save clean users to a CSV file
with open("clean_users.csv", "w", newline="") as clean_file:
    writer = csv.DictWriter(clean_file, fieldnames=["name", "email"])
    writer.writeheader()
    writer.writerows(valid_users)

# 🧾 Save invalid users to a TXT file
with open("invalid_users.txt", "w") as invalid_file:
    invalid_file.write("Invalid Users Report\n")
    for entry in invalid_users:
        invalid_file.write(f"{entry}\n")

# 📊 Final Summary
print("\n✅ Clean Users:")
for user in valid_users:
    print(f"  - {user['name']} | {user['email']}")

print("\n❌ Invalid Users:")
for entry in invalid_users:
    print(f"  - {entry}")