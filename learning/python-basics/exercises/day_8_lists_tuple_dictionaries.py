# Lists vs Tuples vs Dictionaries

# A list: ordered, editable
animals_list = ["cat", "dog", "bird"]
animals_list[0] = "lion"
print("List:", animals_list)

# A tuple: ordered, NOT editable
animals_tuple = ("cat", "dog", "bird")
# animals_tuple[0] = "lion"  # ❌ Will crash if uncommented
print("Tuple:", animals_tuple)

# A dictionary: key-value pairs
animals_dict = {
    "pet1": "cat",
    "pet2": "dog",
    "pet3": "bird"
}
animals_dict["pet1"] = "lion"  # ✅ We can reassign values
print("Dictionary:", animals_dict)
