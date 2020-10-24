def conta_a(string):
    i = 0
    quant_a = 0
    string2 = string.lower()
    while i < len(string):
        if string2[i] == 'a':
            quant_a += 1
        i += 1
    
    return quant_a
