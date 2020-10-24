def encontra_maximo (matrix):
    max_number = 0
    
    for line in matrix:
        for number in line:
            absolute = abs(number)
            
            if absolute > max_number:
                max_number = absolute