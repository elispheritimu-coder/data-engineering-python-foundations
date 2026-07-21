import csv

def is_valid_email(email: str) -> bool:
    email = email.strip().lower()
    return ("@" in email) and ("." in email)

def validate_user(name: str, email: str):
    name = name.strip()
    email = email.strip()

    if not name:
        return False, "Missing name"
    if not name.replace(" ", "").isalpha():
        return False, "Invalid name (letters only)"
    
    if not email:
        return False, "Missing email"
    if not is_valid_email(email):
        return False, "Invalid email format (needs @ and .)"
    return True, "OK"

def process_csv(input_file: str):
    clean_users = []
    invalid_users = []

    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row.get("name", "")
            email = row.get("email", "")

            is_valid, reason = validate_user(name, email)

            if is_valid:
                clean_users.append({
                    "name": name.strip(),
                    "email": email.strip().lower()
                })
            else:
                invalid_users.append({
                    "name": name.strip() or "N/A",
                    "email": email.strip() or "N/A",
                    "reason": reason
                })

    return clean_users, invalid_users

def export_clean_users(clean_users, filename: str):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email"])
        writer.writeheader()
        writer.writerows(clean_users)

def export_invalid_users(invalid_users, filename: str):
    with open(filename, "w") as file:
        file.write("Invalid Users Report\n")
        for user in invalid_users:
            file.write(f"{user['name']} | {user['email']} | {user['reason']}\n")
def count_reasons(invalid_users):
    reason_counts = {}

    for user in invalid_users:
        reason = user["reason"]
        reason_counts[reason] = reason_counts.get(reason, 0) + 1

    return reason_counts

def main():
    input_file = "raw_user_day_11.csv"

    clean_users, invalid_users = process_csv("raw_user_day_11.csv")

    export_clean_users(clean_users, "clean_users_day11.csv")
    export_invalid_users(invalid_users, "invalid_users_day11.txt")

    reason_counts = count_reasons(invalid_users)
    
    print("\n📊 Summary")
    print(f"Total processed: {len(clean_users) + len(invalid_users)}")
    print(f"✅ Clean users: {len(clean_users)}")
    print(f"❌ Invalid users: {len(invalid_users)}")

    print("\n🔎 Invalid Breakdown:")
    for reason, count in reason_counts.items():
        print(f"{reason}: {count}")

main() 