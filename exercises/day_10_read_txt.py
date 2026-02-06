#read user data from raw_users.txt
with open("raw_users.txt", "r") as file:
    lines = file.readlines()
    #strip empty lines first
valid_lines = [line.strip() for line in lines if line.strip()]

#display each raw line 
for line in lines:
    print(f"raw line: {line}")

#want to print a select number of lines Display first 3 lines 
for line in valid_lines:
    print("first 3 :, {line}")

#count how many lines are in the file 
print("total lines in file:",len(lines))

# Filter only clean lines
# Now enumerate only clean lines
for i, line in enumerate(valid_lines, start=1):
    print(f"Valid Line {i}: {line}")
