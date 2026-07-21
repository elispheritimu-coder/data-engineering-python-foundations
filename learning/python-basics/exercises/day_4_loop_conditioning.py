while True:
    raw = input("enter a number (or 'q' to quit):")

    if raw == "q":
        print("Goodbye.")
        break

    try:
        number = int(raw)
        print("you entered:", number)

    except ValueError:
        print("Invalid Input")

