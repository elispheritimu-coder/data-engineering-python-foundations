#identify users with missingemails,invalid emmails
#detect inactive users 
#group and displayflagged users in a summary reprt 

users = [
    {"username": "queen_ellie", "email": "ellie@castle.com", "status": "active"},
    {"username": "ghost", "email": "", "status": "active"},
    {"username": "vibez_nova", "email": "vibez.com", "status": "inactive"},
    {"username": "data_wolf", "email": "wolf@data.ai", "status": "inactive"},
    {"username": "mystery_user", "status": "inactive"},
]

# 🛡️ Container for invalid/suspicious user records
invalid_users = []

for user in users:
    email = user.get("email", "")
    status = user.get("status", "")
    
    # Flag users with invalid email or inactive status
    if not email or "@" not in email or status == "inactive":
        invalid_users.append(user)

# 🧾 Summary Report of Flagged Users
print("\nSuspicious / Inactive User Report:")
print(f"\n📦 Total invalid users found: {len(invalid_users)}")
print("📋 Listing them:") 
for flagged_user in invalid_users:
    print(f" - Username: {flagged_user.get('username', 'unknown')}, "
          f"Email: {flagged_user.get('email', 'not provided')}, "
          f"Status: {flagged_user.get('status', 'not set')}")
    