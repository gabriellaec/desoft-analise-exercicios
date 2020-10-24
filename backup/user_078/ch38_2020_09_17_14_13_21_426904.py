
def quantos_uns(numero):
    i = 0
    quantd = 0
    
    var1 = numero
    var2 = str(var1)

    while i < len(var2):
        
        if var2[i] == '1':
            quantd += 1
            i += 1

        else:
            i += 1
    return quantd