"""
DAY 13 — BLOCK 5
Configurable Validation Pipeline with Dynamic Output Naming + Report File

What this script does:
1. Reads a CSV file from inputs/
2. Cleans and validates users
3. Splits users into clean vs invalid
4. Exports:
   - clean users CSV
   - invalid users TXT
   - report TXT
5. Uses a config section at the top for reusable settings

This is a more job-ready structure because:
- changeable settings are centralized
- output names are generated automatically
- the pipeline leaves behind a readable report
"""

import csv


# =====================================
# CONFIGURATION SECTION
# =====================================

INPUT_FOLDER = "inputs"
OUTPUT_FOLDER = "outputs"

FILE_EXTENSION = ".csv"

CLEAN_PREFIX = "clean_"
INVALID_PREFIX = "invalid_"
REPORT_PREFIX = "report_"


# =====================================
# READ CSV
# =====================================

def read_users_csv(path: str) -> list[dict]:
    """
    Reads CSV into a list of dictionaries.
    Each row becomes one dictionary.
    """
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


# =====================================
# HELPER FUNCTIONS
# =====================================

def is_valid_email(email: str) -> bool:
    """
    Basic email validation:
    - must contain '@'
    - must contain '.'
    - must not contain spaces
    """
    email = email.strip().lower()

    if " " in email:
        return False

    return ("@" in email) and ("." in email)


def normalize_phone(raw_phone: str) -> str:
    """
    Cleans phone number formatting by removing:
    - spaces
    - dashes
    - parentheses
    """
    phone = (raw_phone or "").strip()
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")
    phone = phone.replace("(", "")
    phone = phone.replace(")", "")

    return phone


def standardize_phone(phone: str) -> str | None:
    """
    Accept both:
    - 10-digit local format: 0712345678
    - 12-digit format: 254712345678
    - +254 format: +254712345678

    Standard output format:
    - always 12 digits starting with 254

    Returns:
        standardized phone if valid
        None if invalid
    """
    phone = normalize_phone(phone)

    if phone.startswith("+"):
        phone = phone[1:]

    if not phone.isdigit():
        return None

    if len(phone) == 12 and phone.startswith("254"):
        return phone

    if len(phone) == 10 and phone.startswith("0"):
        return "254" + phone[1:]

    return None


# =====================================
# VALIDATION
# =====================================

def validate_user(name: str, email: str, phone: str) -> tuple[bool, str]:
    """
    Validation rules:
    - name required
    - email required
    - email format must be valid
    - phone required
    - phone must be convertible to accepted format

    Returns:
        (True, "OK") if valid
        (False, "Reason") if invalid
    """
    name = (name or "").strip()
    email = (email or "").strip().lower()
    phone = (phone or "").strip()

    if not name:
        return False, "Missing name"

    if not email:
        return False, "Missing email"

    if not is_valid_email(email):
        return False, "Invalid email format"

    if not phone:
        return False, "Missing phone"

    standardized_phone = standardize_phone(phone)
    if standardized_phone is None:
        return False, "Invalid phone format"

    return True, "OK"


# =====================================
# SPLIT USERS
# =====================================

def split_users(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Splits data into:
    - clean_users
    - invalid_users (with reasons)
    """
    clean_users = []
    invalid_users = []

    for row in rows:
        name = row.get("name", "")
        email = row.get("email", "")
        phone = row.get("phone", "")

        is_valid, reason = validate_user(name, email, phone)

        if is_valid:
            clean_users.append({
                "name": name.strip().title(),
                "email": email.strip().lower(),
                "phone": standardize_phone(phone) or "N/A"
            })
        else:
            invalid_users.append({
                "name": name.strip() or "N/A",
                "email": email.strip() or "N/A",
                "phone": normalize_phone(phone) or "N/A",
                "reason": reason
            })

    return clean_users, invalid_users


# =====================================
# ANALYTICS
# =====================================

def analyze_invalid_reasons(invalid_users: list[dict]) -> dict:
    """
    Counts how many times each invalid reason appears.
    Returns a dictionary like:
    {
        "Missing name": 1,
        "Invalid email format": 2
    }
    """
    reason_counts = {}

    for user in invalid_users:
        reason = user["reason"]
        reason_counts[reason] = reason_counts.get(reason, 0) + 1

    return reason_counts


# =====================================
# EXPORT FUNCTIONS
# =====================================

def export_clean_users(clean_users: list[dict], path: str) -> None:
    """
    Saves clean users to CSV.
    """
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "phone"])
        writer.writeheader()
        writer.writerows(clean_users)


def export_invalid_users(invalid_users: list[dict], path: str) -> None:
    """
    Saves invalid users to TXT with reasons.
    """
    with open(path, "w") as f:
        f.write("Invalid Users Report\n")

        for user in invalid_users:
            f.write(
                f"{user['name']} | {user['email']} | "
                f"{user['phone']} | Reason: {user['reason']}\n"
            )


def write_report(file_name: str, total: int, clean_count: int, invalid_count: int, issue_summary: dict) -> None:
    """
    Writes a human-readable summary report to TXT.
    """
    base_name = file_name.replace(FILE_EXTENSION, "")
    report_path = f"{OUTPUT_FOLDER}/{REPORT_PREFIX}{base_name}.txt"

    with open(report_path, "w") as file:
        file.write(f"File Processed: {file_name}\n")
        file.write(f"Total Records: {total}\n")
        file.write(f"Clean Users: {clean_count}\n")
        file.write(f"Invalid Users: {invalid_count}\n")

        file.write("\n--- Issue Breakdown ---\n")
        for issue, count in issue_summary.items():
            file.write(f"{issue}: {count}\n")


# =====================================
# SUMMARY PRINTING
# =====================================

def print_summary(file_name: str, clean_users: list[dict], invalid_users: list[dict], issue_summary: dict) -> None:
    """
    Prints summary to terminal.
    """
    total = len(clean_users) + len(invalid_users)

    print("\n📊 Summary")
    print(f"File processed: {file_name}")
    print(f"Total processed: {total}")
    print(f"✅ Clean users: {len(clean_users)}")
    print(f"❌ Invalid users: {len(invalid_users)}")

    print("\n📊 Invalid Reason Breakdown")
    for issue, count in issue_summary.items():
        print(f"{issue}: {count}")


# =====================================
# MAIN PIPELINE
# =====================================

def main() -> None:
    """
    Main pipeline:
    - define input file
    - read rows
    - split clean vs invalid
    - analyze invalid reasons
    - generate dynamic output names
    - export outputs
    - print summary
    """
    input_file_name = "day_13_customer_data_.csv"
    input_path = f"{INPUT_FOLDER}/{input_file_name}"

    # create base name dynamically from input
    base_name = input_file_name.replace(FILE_EXTENSION, "")

    clean_output_path = f"{OUTPUT_FOLDER}/{CLEAN_PREFIX}{base_name}.csv"
    invalid_output_path = f"{OUTPUT_FOLDER}/{INVALID_PREFIX}{base_name}.txt"

    rows = read_users_csv(input_path)
    clean_users, invalid_users = split_users(rows)

    issue_summary = analyze_invalid_reasons(invalid_users)

    export_clean_users(clean_users, clean_output_path)
    export_invalid_users(invalid_users, invalid_output_path)

    write_report(
        file_name=input_file_name,
        total=len(rows),
        clean_count=len(clean_users),
        invalid_count=len(invalid_users),
        issue_summary=issue_summary
    )

    print_summary(
        file_name=input_file_name,
        clean_users=clean_users,
        invalid_users=invalid_users,
        issue_summary=issue_summary
    )


main()