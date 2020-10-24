string = 'banana nanica'
def conta_biagramas(string):
    soma_1 = 0
    soma_2 = 0
    soma_3 = 0
    soma_4 = 0
    soma_5 = 0
    soma_6 = 0
    soma_7 = 0
    soma_8 = 0
    i = 1
    dicio = {}
    while i < len(string):
        string_2 = string[i-1] + string[i] 
        if string_2 == 'ba' :
            soma_1 = soma_1 + 1
        elif string_2 == 'an' :
            soma_2 = soma_2 + 1
        elif string_2 == 'na':
            soma_3 = soma_3 + 1
        elif string_2 == 'a ':
            soma_4 = soma_4 + 1
        elif string_2 == ' n':
            soma_5 = soma_5 + 1
        elif string_2 == 'ni':
            soma_6 = soma_6 + 1
        elif string_2 == 'ca':
            soma_7 = soma_7 + 1
        dicio['ba'] = soma_1
        dicio['an'] = soma_2
        dicio['na'] = soma_3
        dicio['a '] = soma_4
        dicio[' n'] = soma_5
        dicio['ni'] = soma_6
        dicio['ca'] = soma_7
        i = i + 1
    return dicio