#mini-drill to test your grip on .get(), not user.get(), and .items().
users = [
    {"username": "queen_ellie", "email": "ellie@castle.com", "country": "Kenya"},
    {"username": "ghost", "country": "unknown"},
    {"email": "no_name@nowhere.com", "status": "inactive"},
    {}
]
for user in users:

    # to fetch the email ,username 
    email = user.get("email", " no email found")
    username = user.get("username", "unnamed")

    print(f"\nAudit for: {username}")
    print(f"Email: {email}")

    #flag empty email/invalid 

    if "@" not in email:
        print("invalid email format")

    #to ffetch the usernames  and flag users without/missing  user name using:
    # not user .get("Username")
    if not user .get("username"):
        print("Missing username.")
    for field, value in user.items():   #dynamic field reporting
        print(f"{field.title()}: {value}")