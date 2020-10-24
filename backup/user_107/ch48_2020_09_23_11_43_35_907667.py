def eh_crescente (numbers):
    if len(numbers) <= 1:
        return False
    
    result = [ numbers[0] ]
    
    for number in numbers[1:]:
        if number > result[-1]:
            result.append(number)
            
    return len(numbers) > 1
