def quantos_uns (value):
    number = str(value)

    count = 0
    for digit in number:
        if digit == "1":
            count += 1
            
    return count