import json
from datetime import datetime


# =========================
# LOG FUNCTION
# =========================
from datetime import datetime

def write_log(level: str, message: str):
    """
    Writes a timestamped log entry with a level.
    Example:
    [2026-03-23 15:30:01] INFO - Pipeline started
    """
    log_file = "logs/pipeline.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {level} - {message}\n"

    with open(log_file, "a") as file:
        file.write(log_entry)
        

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
# EXPORT
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
    try:
        file_path = "inputs/day_14_users.json"

        write_log("INFO","Pipeline started")
        write_log("INFO",f"Reading file: {file_path}")

        users = read_json_file(file_path)

        clean_users, invalid_users = split_users(users)

        clean_path = "outputs/clean_day15.json"
        invalid_path = "outputs/invalid_day15.json"

        export_clean_json(clean_users, clean_path)
        export_invalid_json(invalid_users, invalid_path)

        write_log("INFO",f"Clean users: {len(clean_users)}")
        write_log("INFO",f"Invalid users: {len(invalid_users)}")
        write_log("INFO","Pipeline completed successfully")

        print("Pipeline completed successfully.")

    except Exception as e:
        write_log(f"ERROR", f"{e}")
        print(f"Error: {e}")


main()