import csv


# ==================================================
# FILE PATHS
# ==================================================
# These paths are relative to the project root.
INPUT_FILE = "drills/inputs/clinic_raw.csv"
CLEAN_FILE = "drills/outputs/clinic_clean.csv"
REJECT_FILE = "drills/outputs/clinic_rejects.txt"

# ==================================================
# READ THE RAW CSV
# ==================================================
def read_clinic_data(file_path: str) -> list[dict]:
    """
    Opens the raw CSV file and converts every row
    into a Python dictionary.
    """

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        records = list(reader)

    return records


# ==================================================
# TRANSFORM ONE RECORD
# ==================================================
def transform_record(record: dict) -> dict:
    """
    Cleans and standardizes one record.

    - Removes extra spaces from every field
    - Changes email to lowercase
    - Capitalizes the department consistently
    """

    transformed_record = {
        "name": record.get("name", "").strip(),
        "age": record.get("age", "").strip(),
        "email": record.get("email", "").strip().lower(),
        "department": record.get("department", "").strip().title()
    }

    return transformed_record


# ==================================================
# VALIDATE ONE RECORD
# ==================================================
def validate_record(record: dict) -> list[str]:
    """
    Checks one transformed record against all rules.

    Returns a list of failure reasons.
    An empty list means the record is valid.
    """

    reasons = []

    name = record["name"]
    age = record["age"]
    email = record["email"]
    department = record["department"]

    # Name must not be empty
    if not name:
        reasons.append("missing name")

    # Age must exist
    if not age:
        reasons.append("missing age")

    # Age must contain digits only
    elif not age.isdigit():
        reasons.append("age is not a number")

    # Age must be between 18 and 99
    else:
        age_number = int(age)

        if age_number < 18:
            reasons.append("underage")

        elif age_number > 99:
            reasons.append("age above allowed range")

    # Email must contain @
    if "@" not in email:
        reasons.append("bad email")

    else:
        # Split at the first @ and check the part after it
        email_parts = email.split("@", 1)
        domain = email_parts[1]

        if "." not in domain:
            reasons.append("bad email")

    # Department must not be empty
    if not department:
        reasons.append("missing department")

    return reasons


# ==================================================
# PROCESS ALL RECORDS
# ==================================================
def process_records(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Transforms and validates every record.

    Valid records go into valid_records.
    Invalid records go into invalid_records with reasons.
    """

    valid_records = []
    invalid_records = []

    for record in records:
        transformed_record = transform_record(record)
        reasons = validate_record(transformed_record)

        if not reasons:
            valid_records.append(transformed_record)

        else:
            rejected_record = transformed_record.copy()
            rejected_record["reasons"] = reasons
            invalid_records.append(rejected_record)

    return valid_records, invalid_records


# ==================================================
# EXPORT VALID RECORDS
# ==================================================
def export_clean_records(records: list[dict], file_path: str) -> None:
    """
    Writes valid transformed records to a CSV file.
    """

    fieldnames = ["name", "age", "email", "department"]

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(records)


# ==================================================
# EXPORT REJECTED RECORDS
# ==================================================
def export_rejected_records(records: list[dict], file_path: str) -> None:
    """
    Writes rejected records to a TXT file,
    including every reason each record failed.
    """

    with open(file_path, "w") as file:
        file.write("CLINIC REJECTED RECORDS\n")
        file.write("=======================\n\n")

        for record in records:
            reasons_text = ", ".join(record["reasons"])

            file.write(
                f"Name: {record['name'] or 'N/A'} | "
                f"Age: {record['age'] or 'N/A'} | "
                f"Email: {record['email'] or 'N/A'} | "
                f"Department: {record['department'] or 'N/A'} | "
                f"Reasons: {reasons_text}\n"
            )


# ==================================================
# COUNT FAILURE REASONS
# ==================================================
def count_failure_reasons(invalid_records: list[dict]) -> dict:
    """
    Counts how many times each validation failure occurred.
    """

    reason_counts = {}

    for record in invalid_records:
        for reason in record["reasons"]:
            reason_counts[reason] = reason_counts.get(reason, 0) + 1

    return reason_counts


# ==================================================
# PRINT TERMINAL REPORT
# ==================================================
def print_report(
    total_records: int,
    valid_records: list[dict],
    invalid_records: list[dict],
    reason_counts: dict
) -> None:
    """
    Prints totals, percentages and failure reasons.
    """

    valid_count = len(valid_records)
    invalid_count = len(invalid_records)

    if total_records > 0:
        valid_percentage = valid_count / total_records * 100
        invalid_percentage = invalid_count / total_records * 100
    else:
        valid_percentage = 0
        invalid_percentage = 0

    print("\nCLINIC DATA PURGE REPORT")
    print("========================")
    print(f"Total records: {total_records}")
    print(f"Valid records: {valid_count} ({valid_percentage:.1f}%)")
    print(f"Invalid records: {invalid_count} ({invalid_percentage:.1f}%)")

    print("\nFailure breakdown:")

    if reason_counts:
        for reason, count in reason_counts.items():
            print(f"- {reason}: {count}")
    else:
        print("- No validation failures")


# ==================================================
# MAIN PIPELINE
# ==================================================
def main() -> None:
    """
    Controls the complete pipeline in order.
    """

    print("Starting clinic data purge...")

    # Stage 1: Read
    records = read_clinic_data(INPUT_FILE)

    # Stage 2–4: Transform, validate and split
    valid_records, invalid_records = process_records(records)

    # Stage 5: Export
    export_clean_records(valid_records, CLEAN_FILE)
    export_rejected_records(invalid_records, REJECT_FILE)

    # Stage 6: Analyze and report
    reason_counts = count_failure_reasons(invalid_records)

    print_report(
        total_records=len(records),
        valid_records=valid_records,
        invalid_records=invalid_records,
        reason_counts=reason_counts
    )

    print("\nClinic data purge completed.")


main()