list = []

while True:
    str_number = input("Number? ")
    number = int(str_number)
    
    if number <= 0:
        break
    else:
        list.append(number)

for number in reversed(list):
    print(number)
