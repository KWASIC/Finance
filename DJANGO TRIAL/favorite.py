import csv

with open ("favorite.csv","r") as file:
    reader = csv.DictReader(file)
    scratch,c,python = 0,0,0

    for row in reader:
        favorite = row["language"]
        if favorite == "scratch":
            scratch += 1
        elif favorite == "c":
            c += 1
        elif favorite == "python":
            python += 1

print(f" Scratch: {scratch}")
print(f" C: {c}")
print(f" Python: {python}")
