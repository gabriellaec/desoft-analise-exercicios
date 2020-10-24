result = 0

is_asking = True
while is_asking:
    number = float(input("Número? "))
    
    if number == 0:
        break
    
    result += number

print(result)
