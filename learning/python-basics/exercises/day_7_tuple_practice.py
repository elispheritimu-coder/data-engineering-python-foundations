# 👑 Tuple Practice: Royal Pets Registry

# Each pet tuple: (name, species, age)
pets = [
    ("Zuri", "cat", 2),
    ("Bolt", "dog", 4),
    ("Nia", "parrot", 1),
    ("Rex", "dog", 8),
    ("Mimi", "cat", 3)
]

# Let's analyze them
for name, species, age in pets:
    print(f"\n{name} is a {species}, aged {age}.")

    if species == "dog" and age < 5:
        print("💡 Young dog — consider training classes.")
    elif species == "dog" and age >= 5:
        print("🛡️ Mature dog — ensure regular vet visits.")
    elif species == "cat":
        print("🐾 Cat — schedule claw trimming.")
    elif species == "parrot":
        print("🦜 Parrot — check talking progress!")

# ✅ Summary
print(f"\nYou just processed {len(pets)} royal pets using tuples!")
