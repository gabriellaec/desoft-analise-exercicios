def quantos_uns(palavra):
    i=0
    contador=0
    while i<len(palavra):
        if palavra[i]=='1':
            contador+=1
        i+=1
    return contador
palavra=str(input('Escreva um número: '))