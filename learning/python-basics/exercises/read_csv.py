# Day 10 Block 2 – Read CSV and validate user emails
# Day 10 Block 2 – Read CSV and validate user emails

valid_users = []  # container for clean records

with open("raw_user.csv", "r") as file:
    lines = file.readlines()

if not lines:
    print("The CSV file is empty. No data to process.")
else:
    header = lines[0].strip()
    data_lines = lines[1:]

    print("\n📋 Valid Users:")
    for line in data_lines:
        cleaned = line.strip()
        if not cleaned:
            continue  # skip blanks

        parts = cleaned.split(",")
        if len(parts) != 2:
            print(f"⚠️ Skipping malformed row: {cleaned}")
            continue

        name, email = parts[0].strip(), parts[1].strip()

        if "@" in email and "." in email:
            print(f"✅ Valid user: {name}, Email: {email}")
            valid_users.append((name, email))
        else:
            print(f"❌ Invalid Email for {name} → {email}")

    # Save valid users to .txt
    with open("valid_users.txt", "w") as txt_file:
        txt_file.write("Valid Users List\n")
        for name, email in valid_users:
            txt_file.write(f"{name}, {email}\n")

    # Save valid users to .csv
    with open("valid_users.csv", "w") as csv_file:
        csv_file.write("Name,Email\n")
        for name, email in valid_users:
            csv_file.write(f"{name},{email}\n")

    print(f"\n📁 Saved {len(valid_users)} valid users to 'valid_users.txt' and 'valid_users.csv'")