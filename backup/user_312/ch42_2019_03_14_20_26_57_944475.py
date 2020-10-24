def quantos_uns(numero):
    contador=0
    string=str(numero)
    tamanho=len(string)
    i=0
    while i<tamanho:
        if string[tamanho]=='1':
            contador+=1
        i+=1
    return contador