import csv


def read_users_csv(path: str) -> list[dict]:
    """Read CSV into a list of dict rows."""
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def normalize_user(row: dict) -> dict:
    """Clean/standardize raw values (strip spaces, lower email)."""
    name = (row.get("name") or "").strip()
    email = (row.get("email") or "").strip().lower()

    return {"name": name, "email": email}


def validate_user(user: dict) -> tuple[bool, str]:
    """Return (is_valid, reason). Keep rules simple for Block 1."""
    name = user["name"]
    email = user["email"]

    if not name:
        return False, "Missing name"
    if not email:
        return False, "Missing email"
    if "@" not in email or "." not in email:
        return False, "Invalid email format"
    return True, "OK"


def split_users(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """Normalize + validate each row and split into clean vs invalid lists."""
    clean_users = []
    invalid_users = []

    for row in rows:
        user = normalize_user(row)
        is_valid, reason = validate_user(user)

        if is_valid:
            clean_users.append(user)
        else:
            invalid_users.append(
                {"name": user["name"] or "N/A", "email": user["email"] or "N/A", "reason": reason}
            )

    return clean_users, invalid_users


def export_clean_users(clean_users: list[dict], path: str) -> None:
    """Write clean users to CSV."""
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email"])
        writer.writeheader()
        writer.writerows(clean_users)


def export_invalid_users(invalid_users: list[dict], path: str) -> None:
    """Write invalid users to TXT with reasons."""
    with open(path, "w") as f:
        f.write("Invalid Users Report\n")
        for u in invalid_users:
            f.write(f"{u['name']} | {u['email']} | Reason: {u['reason']}\n")


def print_summary(clean_users: list[dict], invalid_users: list[dict]) -> None:
    total = len(clean_users) + len(invalid_users)
    print("\n📊 Summary")
    print(f"Total processed: {total}")
    print(f"✅ Clean users: {len(clean_users)}")
    print(f"❌ Invalid users: {len(invalid_users)}")


def main() -> None:
    input_file = "exercises/day_12_raw_data.csv"
    clean_out = "clean_users_day12.csv"
    invalid_out = "invalid_users_day12.txt"

    rows = read_users_csv(input_file)
    clean_users, invalid_users = split_users(rows)

    export_clean_users(clean_users, clean_out)
    export_invalid_users(invalid_users, invalid_out)
    print_summary(clean_users, invalid_users)


main()