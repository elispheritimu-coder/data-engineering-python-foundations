# 📜 Day 10 Log — Data Validation and Cleanup from Text & CSV Files

## ✅ Goals for Day 10
- Read data from `.txt` and `.csv` files.
- Strip and validate real-world user entries.
- Skip malformed or empty lines.
- Validate name and email fields.
- Save clean and invalid records to appropriate files.
- Track reasons for invalidation.
- Practice structured logging and exports in text and CSV formats.

---

## 📂 Block 1 — Read and Display `.txt` File
**Objective:** Understand file reading in Python.

- Opened a `.txt` file using `with open()`.
- Printed all raw lines.
- Stripped whitespace and skipped empty lines.
- Displayed valid lines with line numbers.

---

## 📂 Block 2 — Validate and Export Clean Entries from `.txt`
**Objective:** Identify clean vs. malformed records and export them.

- Cleaned and validated lines (must contain a comma, name, and email).
- Checked for valid email format (`@` and `.` present).
- Exported clean users to `clean_users.txt` and `clean_users.csv`.
- Flagged invalid records to `invalid_users.txt`.

---

## 📂 Block 3 — Parse `.csv`, Convert to Dictionary
**Objective:** Read and validate CSV into structured dictionaries.

- Read `raw_user.csv`, skipped header.
- Parsed each line into a `dict`: `{"name": name, "email": email}`.
- Appended valid user dictionaries to a list.
- Printed clean user summary.

---

## 📂 Block 4 — Log Invalid Users with Reasons
**Objective:** Record validation failures with explanations.

- For every invalid line, provided a reason:
  - Missing fields
  - Invalid email format
- Exported to `invalid_users_b4.txt` for transparency.

---

## 📂 Block 5 — Export Valid and Invalid Records
**Objective:** Fully separate and document valid/invalid entries.

- Clean users ➝ `clean_users_b5.csv`
- Invalid users ➝ `invalid_users_b5.csv` and `.txt` with reasons
- Structured validation into reusable `if` logic

---

## 📂 Block 6 — Dynamic Field Matching and Final Cleanup
**Objective:** Ensure field headers match exactly, avoid hardcoding.

- Extracted header fields dynamically (`name`, `email`)
- Used `dict.get()` for safer access
- Final export:
  - Clean users with headers to `clean_users_b6.csv`
  - Invalid users with reasons to `invalid_users_b6.csv` and `.txt`

---

## 🧠 Concepts Mastered Today
- File handling: `with open()` for `.txt` and `.csv`
- Line iteration and cleanup
- Email validation using conditional logic
- Dictionary creation and structured export
- Exporting clean/invalid data to multiple formats
- Logging and tracking errors

---

## 🏁 Status
- ✅ All Blocks (1–6) Completed
- ✅ Clean and Invalid exports working
- ✅ Scripts tested and updated
- ✅ Logs tracked by block

---

**Ready for Day 11: Advanced String Processing and Regular Expressions (Regex)** 👑