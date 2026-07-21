"""

Batch Processing Multiple Files

Objective:
Process ALL CSV files inside inputs/ automatically.

Instead of:
    running script per file

We now:
    loop through all files and process each one
"""

import csv
import os  # new: lets us interact with folders/files


# ===============================
# READ CSV
# ===============================

def read_users_csv(path: str) -> list[dict]:
    with open(path, "r", newline="") as f:
        return list(csv.DictReader(f))


# ===============================
# VALIDATION HELPERS
# ===============================

def is_valid_email(email: str) -> bool:
    email = email.strip().lower()
    return ("@" in email) and ("." in email)


def validate_user(name: str, email: str) -> tuple[bool, str]:
    if not name:
        return False, "Missing name"
    if not email:
        return False, "Missing email"
    if not is_valid_email(email):
        return False, "Invalid email format"
    return True, "OK"


# ===============================
# SPLIT USERS
# ===============================

def split_users(rows: list[dict]):
    clean = []
    invalid = []

    for row in rows:
        name = row.get("name", "").strip()
        email = row.get("email", "").strip()

        is_valid, reason = validate_user(name, email)

        if is_valid:
            clean.append({"name": name, "email": email})
        else:
            invalid.append({
                "name": name or "N/A",
                "email": email or "N/A",
                "reason": reason
            })

    return clean, invalid


# ===============================
# EXPORT
# ===============================

def export_clean(clean_users, path):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email"])
        writer.writeheader()
        writer.writerows(clean_users)


def export_invalid(invalid_users, path):
    with open(path, "w") as f:
        for u in invalid_users:
            f.write(f"{u['name']} | {u['email']} | {u['reason']}\n")


# ===============================
# PROCESS ONE FILE
# ===============================

def process_file(input_path, filename):
    """
    Handles ONE file:
    read → validate → split → export
    """

    rows = read_users_csv(input_path)
    clean, invalid = split_users(rows)

    # create output filenames dynamically
    clean_out = f"outputs/clean_{filename}"
    invalid_out = f"outputs/invalid_{filename.replace('.csv', '.txt')}"

    export_clean(clean, clean_out)
    export_invalid(invalid, invalid_out)

    print(f"\nProcessed: {filename}")
    print(f"Clean: {len(clean)} | Invalid: {len(invalid)}")


# ===============================
# MAIN: LOOP THROUGH FILES
# ===============================

def main():
    input_folder = "inputs"

    # loop through everything in inputs/
    for filename in os.listdir(input_folder):

    if filename.endswith(".csv"):

        full_path = os.path.join(input_folder, filename)

        try:
            process_file(full_path, filename)

        except Exception as e:
            print(f"\n❌ Error processing {filename}: {e}")

            # process each file
            process_file(full_path, filename)


main()