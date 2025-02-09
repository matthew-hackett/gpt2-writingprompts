unfiltered_lines = []
filtered_lines = []

# Open the file
with open("data/unfiltered.txt", "r") as f:
    for line in f.readlines():
        unfiltered_lines.append(line.strip())

# Clear
for ul in unfiltered_lines:
    if "]" in ul:
        i = ul.index("]")
        fl = ul[i+1:].strip()
        fl = fl.replace("``", "\"")
        fl = fl.replace("''", "\"")
        fl = fl.replace("`", "'")
        fl = fl.replace(" .", ".")
        fl = fl.replace(" ,", ",")
        filtered_lines.append(fl + "\n")

# Write lines to new file
with open("data/filtered.txt", "w") as f:
    f.writelines(filtered_lines)