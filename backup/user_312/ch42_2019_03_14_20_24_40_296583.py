def quantos_uns(numero):
    contador=0
    string=str(numero)
    tamanho=len(string)-1
    while tamanho<=string:
        if string[tamanho]=='1':
            contador+=1
    return contador