def eh_crescente(values):
    i = 1
    while i < len(values):
        if values[i] > values[i-1]:
            i+=1
        if values[i] <= values[i-1]:
            i+=1
            return False
    return True
