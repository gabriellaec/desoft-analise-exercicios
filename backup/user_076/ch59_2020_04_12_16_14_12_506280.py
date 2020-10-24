def asteriscos(n):
    i = 0
    string = [0]*1
    while i<n:
        string.append("'"+string[0])
        i+=1
    return string[0]
        