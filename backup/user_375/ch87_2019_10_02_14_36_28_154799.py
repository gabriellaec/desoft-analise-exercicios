with open("churras.txt", "r") as file:
    content = file.read().replace(" ", "").split()

total = 0
i = 0

while i < len(content):
    content[i] = content[i].split(",")
    price = int(content[i][1])
    quant = float(content[i][2])
    total += price * quant
    i += 1

print(total)