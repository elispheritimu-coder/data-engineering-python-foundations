from datetime import datetime


# =========================
# LOG FUNCTION
# =========================
def write_log(message: str):
    """
    Writes a message to a log file with timestamp
    """

    log_file = "logs/pipeline.log"

    # get current time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # format log message
    log_entry = f"[{timestamp}] {message}\n"

    # append to log file
    with open(log_file, "a") as file:
        file.write(log_entry)


# =========================
# TEST
# =========================
def main():
    write_log("Pipeline started")
    write_log("Processing file: test.csv")
    write_log("Pipeline completed successfully")


main()