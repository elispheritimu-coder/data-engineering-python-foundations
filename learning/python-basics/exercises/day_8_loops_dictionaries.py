users = [
    {
        "username": "queen_ellis",
        "email": "ellis@monetize.ai",
        "status": "active",
        "country": "Kenya"
    },
    {
        "username": "data_wolf",
        "email": "",
        "status": "inactive",
        "country": None
    },
    {
        "username": "vibez_nova",
        "status": "active",
        "country": "Nigeria"
    },
    {
        "username": "lyra_ai",
        "email": "lyra@vibez.com",
        "status": "active",
        "country": "Ghana"
    }
]
for user in users:
    print("\n Audit report for:", user.get("username", "unnamed"))
    for field, value in user.items():
        clean_value = value if value else "Missing"
        print(f"{field.title()}: {clean_value}")