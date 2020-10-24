list = []

while True:
    number = int(input("Number? "))
    
    if number >= 0:
        list.append(number)
    else:
        break

for number in reversed(list):
    print(number)
