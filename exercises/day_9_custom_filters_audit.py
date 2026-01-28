#validate :names that contain character only 
#emails that cotain @, end with know domain (.net, .com, .org , .co)
#and are not dummy valuues like (no_email , 'test@unknown.com
users = [
    {"name": "Alice", "email": "alice@gmail.com"},
    {"name": "bob123", "email": "bob_at_gmail.com"},
    {"name": "CHARLIE", "email": "charlie@yahoo.org"},
    {"name": "daisy$", "email": "daisy@yahoo"},
    {"name": "eve", "email": "test@unknown.com"},
    {"name": "frank", "email": "   FRANK@outlook.net   "},
    {"name": "gina", "email": "no_email"},
]

banned_emails = ["no_email", "test@unknown.com"]
valid_domains = [".com", ".org", ".net"]

flagged_users = []

for user in users:
    name = user.get("name", "").strip().title()
    email = user.get("email", "").strip().lower()
    
    name_valid = name.isalpha()
    email_valid = (
        "@" in email and 
        email.endswith(tuple(valid_domains)) and
        email not in banned_emails
    )

    if not name_valid or not email_valid:
        flagged_users.append(user)
        print(f"\n Flagged user:")
        print(f"Name: {name} | Valid: {name_valid}")
        print(f"Email: {email} | Valid: {email_valid}")
    else:
        print(f"\n Clean user: {name} | Email: {email}")
print("total flagged users:", len(flagged_users))