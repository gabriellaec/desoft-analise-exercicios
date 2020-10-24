def quantos_uns (numero):
    string=str(numero)
    i=0
    soma=0
    while i < len(string):
        if string[i] == "1":
            soma +=1
            i+=1
        if string[i] != "1":
            soma=soma 
            i+=1
    return soma 
            