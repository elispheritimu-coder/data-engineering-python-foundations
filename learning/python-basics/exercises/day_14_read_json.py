import json


# =========================
# READ JSON
# =========================
def read_json_file(path: str):
    with open(path, "r") as file:
        return json.load(file)


# =========================
# VALIDATION
# =========================
def is_valid_email(email: str) -> bool:
    email = email.strip().lower()
    return ("@" in email) and ("." in email)


def validate_user(user: dict):
    name = user.get("name", "").strip()
    email = user.get("email", "").strip()

    if not name:
        return False, "Missing name"

    if not email:
        return False, "Missing email"

    if not is_valid_email(email):
        return False, "Invalid email format"

    return True, "OK"


# =========================
# SPLIT USERS
# =========================
def split_users(users):
    clean_users = []
    invalid_users = []

    for user in users:
        is_valid, reason = validate_user(user)

        if is_valid:
            clean_users.append(user)
        else:
            user["reason"] = reason
            invalid_users.append(user)

    return clean_users, invalid_users
# =========================
# EXPORT JSON
# =========================
def export_clean_json(clean_users, path):
    with open(path, "w") as file:
        json.dump(clean_users, file, indent=2)


def export_invalid_json(invalid_users, path):
    with open(path, "w") as file:
        json.dump(invalid_users, file, indent=2)


# =========================
# MAIN
# =========================
def main():
    file_path = "inputs/day_14_users.json"

    users = read_json_file(file_path)

    clean_users, invalid_users = split_users(users)

    # export paths
    clean_path = "outputs/clean_day14.json"
    invalid_path = "outputs/invalid_day14.json"

    export_clean_json(clean_users, clean_path)
    export_invalid_json(invalid_users, invalid_path)

    print("Export complete.")


main()