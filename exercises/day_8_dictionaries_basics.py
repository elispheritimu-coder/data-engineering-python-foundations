# Dictionary Basics

user = {
    "name": "Elispher",
    "age": 27,
    "account_type": "premium"
}

# Regular access
print("Name:", user["name"])
print("Age:", user["age"])


# Add a new field
user["country"] = "Kenya"
print("Updated user:", user)

# Add or update fields
user["last_login"] = "2026-01-20"
user["age"] = 28  # Update

# Safe checks
print("Phone number:", user.get("phone", "No phone listed"))


#print users name and email
#flag users who are in actve
#update missing emails with "not_provided@example.com"
users = [
    {"name": "Elispher", "age": 27, "account_type": "premium", "email": "elispher@data.co", "status": "active"},
    {"name": "Nova", "age": 30, "account_type": "basic", "status": "inactive"},
    {"name": "Jules", "age": 22, "account_type": "premium", "email": "jules@vibez.com", "status": "active"},
    {"name": "Lyra", "age": 35, "account_type": "basic", "email": "lyra@tech.net", "status": "inactive"},
    {"name": "Ken", "age": 29, "account_type": "premium", "status": "active"},
]

for user in users:
    print("\n--- User Info ---")
    print("Name:", user["name"])
    
    # Safe access to email avoids crashing of the script ...it adds what to do if field id empty
    email = user.get("email", "not_provided@example.com")
    print("Email:", email)
    
    # Flag inactive users
    if user["status"] == "inactive":
        print(" This user is INACTIVE")
    
    # Add email if missing #adding a missing field or a new field "email" =[key]
    if "email" not in user:
        user["email"] = "not_provided@example.com"
        print(" Email field added.")

# Final data preview
print("\n✅ All users after audit:")
for user in users:
    print(user)
