"""
DAY 12 — BLOCK 3
Pipeline + Invalid Reason Breakdown Export

What this script does:
1) Reads raw users from inputs/day_12_raw_data.csv
2) Validates name, email, phone
3) Splits into clean vs invalid users
4) Exports:
   - outputs/clean_users_day12_block3.csv
   - outputs/invalid_users_day12_block3.txt
5) Creates an "invalid reasons breakdown" report:
   - outputs/invalid_reason_breakdown_day12_block3.csv
   - Prints breakdown summary to terminal

Key engineering idea:
- Validation rules live in validate_user()
- Analytics lives in analyze_invalid_reasons()
- Exporting analytics lives in export_reason_breakdown()
"""

import csv


# ===============================
# 1) READ CSV
# ===============================

def read_users_csv(path: str) -> list[dict]:
    """Read CSV into a list of dict rows."""
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


# ===============================
# 2) HELPERS: EMAIL + PHONE
# ===============================

def is_valid_email(email: str) -> bool:
    """
    Basic email check:
    - must contain '@' and '.'
    - no spaces
    """
    email = email.strip().lower()
    if " " in email:
        return False
    return ("@" in email) and ("." in email)


def normalize_phone(raw_phone: str) -> str:
    """
    Normalize phone by removing spaces, dashes, parentheses.
    Keep leading '+' if present; we handle it later.
    """
    p = (raw_phone or "").strip()
    p = p.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    return p


def standardize_phone_to_12_digits(phone: str) -> str | None:
    """
    Accept both:
    - 10 digits (0712345678)  -> convert to 12 digits (254712345678)
    - 12 digits (254712345678) -> keep as is
    Also accept:
    - +254712345678 -> convert to 254712345678

    Returns:
        standardized 12-digit phone string, or None if not possible
    """
    p = normalize_phone(phone)

    # remove leading '+'
    if p.startswith("+"):
        p = p[1:]

    # must be digits only at this point
    if not p.isdigit():
        return None

    # already 12 digits
    if len(p) == 12 and p.startswith("254"):
        return p

    # local 10-digit starting with 0 (Kenya style)
    if len(p) == 10 and p.startswith("0"):
        return "254" + p[1:]

    return None


# ===============================
# 3) VALIDATION (RULE GATE)
# ===============================

def validate_user(name: str, email: str, phone: str) -> tuple[bool, str]:
    """
    Rules:
    - name required
    - email required + valid format
    - phone required + must standardize to 12-digit format
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

    standardized = standardize_phone_to_12_digits(phone)
    if standardized is None:
        return False, "Invalid phone (must be 10-digit local or 12-digit 254 format)"

    return True, "OK"


# ===============================
# 4) SPLIT USERS
# ===============================

def split_users(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Creates:
    - clean_users: standardized records
    - invalid_users: record + reason
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
                # store standardized phone (12 digits)
                "phone": standardize_phone_to_12_digits(phone) or "N/A"
            })
        else:
            invalid_users.append({
                "name": name.strip() or "N/A",
                "email": email.strip() or "N/A",
                "phone": normalize_phone(phone) or "N/A",
                "reason": reason
            })

    return clean_users, invalid_users


# ===============================
# 5) EXPORT CLEAN + INVALID
# ===============================

def export_clean_users(clean_users: list[dict], path: str) -> None:
    """Write clean users to CSV."""
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "phone"])
        writer.writeheader()
        writer.writerows(clean_users)


def export_invalid_users(invalid_users: list[dict], path: str) -> None:
    """Write invalid users to TXT with reasons."""
    with open(path, "w") as f:
        f.write("Invalid Users Report\n")
        for u in invalid_users:
            f.write(f"{u['name']} | {u['email']} | {u['phone']} | Reason: {u['reason']}\n")


# ===============================
# 6) ANALYTICS: REASON BREAKDOWN
# ===============================

def analyze_invalid_reasons(invalid_users: list[dict]) -> dict:
    """
    Returns a dictionary:
        { reason: count }
    This is better than printing because it can be reused/exported.
    """
    reason_counts = {}

    for user in invalid_users:
        reason = user["reason"]
        reason_counts[reason] = reason_counts.get(reason, 0) + 1

    return reason_counts


def export_reason_breakdown(reason_counts: dict, path: str) -> None:
    """Export invalid reason counts to CSV."""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["reason", "count"])

        for reason, count in reason_counts.items():
            writer.writerow([reason, count])


def print_reason_breakdown(reason_counts: dict) -> None:
    """Print breakdown to terminal."""
    print("\n📊 Invalid Reason Breakdown")

    for reason, count in reason_counts.items():
        print(f"{reason}: {count}")

    if reason_counts:
        dominant = max(reason_counts, key=reason_counts.get)
        print(f"\n⚠️ Most common issue: {dominant}")


# ===============================
# 7) SUMMARY
# ===============================

def print_summary(clean_users: list[dict], invalid_users: list[dict]) -> None:
    total = len(clean_users) + len(invalid_users)
    print("\n📊 Summary")
    print(f"Total processed: {total}")
    print(f"✅ Clean users: {len(clean_users)}")
    print(f"❌ Invalid users: {len(invalid_users)}")


# ===============================
# 8) MAIN (ORCHESTRATOR)
# ===============================

def main() -> None:
    # Inputs/Outputs kept predictable (professional habit)
    input_file = "inputs/12_raw_data2.csv"

    clean_out = "outputs/clean_users_day12_block3.csv"
    invalid_out = "outputs/invalid_users_day12_block3.txt"
    breakdown_out = "outputs/invalid_reason_breakdown_day12_block3.csv"

    rows = read_users_csv(input_file)
    clean_users, invalid_users = split_users(rows)

    export_clean_users(clean_users, clean_out)
    export_invalid_users(invalid_users, invalid_out)

    # Analytics stage
    reason_counts = analyze_invalid_reasons(invalid_users)
    export_reason_breakdown(reason_counts, breakdown_out)

    # Terminal reporting
    print_summary(clean_users, invalid_users)
    print_reason_breakdown(reason_counts)


main()