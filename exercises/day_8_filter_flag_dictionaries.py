#create audit flags onlyfor users with problems like :
#missing email
#inactive status
#missing country
#only display messages only when there are issues 
users = [
    {"username": "queen_ellis", "email": "ellis@monetize.ai", "status": "active", "country": "Kenya"},
    {"username": "data_wolf", "email": "", "status": "inactive", "country": None},
    {"username": "vibez_nova", "status": "active"},  # missing email and country
    {"username": "lyra_ai", "email": "lyra@vibez.com", "status": "active", "country": "Ghana"}
]

for user in users:
    print(f"\nAudit report for: {user.get('username', 'Unnamed User')}")
    
    flags = []  # empty list to collect issues
    
    # Check for missing email
    if not user.get("email"):
        flags.append("Missing email")
    
    # Check for inactive account
    if user.get("status") == "inactive":
        flags.append("Inactive account")
    
    # Check for missing country
    if not user.get("country"):
        flags.append("Country not provided")
    
    # Display only if there are any flags
    if flags:
        print("⚠️ Issues found:")
        for flag in flags:
            print("-", flag)
    else:
        print("✅ All user info looks good!")

#Audits and metrics 
#totals of :users processed,missing emails,inactive,no country


users = [
    {"username": "queen_ellis", "email": "ellis@monetize.ai", "status": "active", "country": "Kenya"},
    {"username": "data_wolf", "email": "", "status": "inactive", "country": None},
    {"username": "vibez_nova", "status": "active"},  # missing email and country
    {"username": "lyra_ai", "email": "lyra@vibez.com", "status": "active", "country": "Ghana"}
]

# Initialize counters
total_users = 0
missing_emails = 0
inactive_users = 0
missing_countries = 0

for user in users:
    total_users += 1
    print(f"\nAudit report for: {user.get('username', 'Unnamed User')}")

    flags = []

    if not user.get("email"):
        flags.append("Missing email")
        missing_emails += 1
    
    if user.get("status") == "inactive":
        flags.append("Inactive account")
        inactive_users += 1

    if not user.get("country"):
        flags.append("Country not provided")
        missing_countries += 1

    if flags:
        print("⚠️ Issues found:")
        for flag in flags:
            print("-", flag)
    else:
        print("✅ All user info looks good!")

# Final summary
print("\n—— Final Summary ——")
print("Total users audited:", total_users)
print("Users with missing emails:", missing_emails)
print("Inactive users:", inactive_users)
print("Users missing country info:", missing_countries)
