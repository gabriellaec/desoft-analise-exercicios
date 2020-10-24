list = []

while True:
    str_number = input("Number? ")
    
    if not str_number:
        continue
    
    number = int(str_number)
    
    if number < 0:
        break
    else:
        list.append(number)

for number in reversed(list):
    print(number)
