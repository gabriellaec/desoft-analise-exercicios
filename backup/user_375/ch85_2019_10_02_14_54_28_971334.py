with open("macacos-me-mordam.txt", "r") as file:
    content = file.read().rstrip().lower().split()

counter = 0
i = 0

while i < len(content):
    if content[i] == "banana":
        counter += 1
    i += 1

print(counter)
