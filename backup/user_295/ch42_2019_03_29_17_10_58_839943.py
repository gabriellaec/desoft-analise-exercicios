def quantos_uns (numero):
    texto = str (numero)
    i=0
    x=0
    while i < len(texto):
        if texto [i] == "1":
            x += 1
        i +=1    
    return x

