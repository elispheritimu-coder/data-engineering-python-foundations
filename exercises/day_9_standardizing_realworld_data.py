#Let’s say you are reviewing signups, and you want to clean up the "country" fields.

users = [
    {"name": "Alice", "country": " Kenya "},
    {"name": "Bob", "country": "kenya"},
    {"name": "Charlie", "country": "KenYa"},
    {"name": "Daisy", "country": " United States "},
    {"name": "Eve", "country": "  nigeria"}
]
flagged_country_users = []
for user in users:
    raw_country = user.get("country", "Unknown")

    #clean:Remove whitespace ,convert to title case 
    clean_country = raw_country.strip().title()
    flagged_country_users.append(user)


    #save cleaned version back into dictionary 
    user["country"] = clean_country
    print(f"{user['name']} | country(cleaned):{clean_country} ")
print(f"\total cleaned countries:", {len(flagged_country_users)})#counts all cleaned


#cleanining names and emails 

users = [
    {"name": "alice", "email": " ALICE@GMAIL.COM "},
    {"name": "BOB", "email": "bob@Gmail.Com"},
    {"name": "charlie", "email": "  CHARLIE@YAHOO.COM"},
    {"name": "DAISY", "email": " DAISY@Yahoo.com "}
]
flagged_emails = []
flagged_name = []
for user in users:
    raw_name = user.get("name", "Unknown")
    raw_email = user.get("email", "No Email")

    clean_name = raw_name.strip().title()
    clean_email = raw_email.strip().lower()

    flagged_emails.append(user)
    flagged_name.append(user)

    user["name"] = clean_name
    user["email"] = clean_email

    print(f"{clean_name} | Email: {clean_email}")
print("Total of clean names:", len(flagged_name) , "Total clean emai:", len(flagged_emails))