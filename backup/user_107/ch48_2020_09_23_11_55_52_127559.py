def eh_crescente (numbers):
    i = 0
    while(i < len(numbers) - 1):
        number = numbers[i]
        next_number = numbers[i + 1]

        if not number < next_number:
            return False

        i += 1
        
    return True