with open('palavras.txt','r') as arquivo:

    documento = arquivo.read().split()
    lista_separada = []
    contador = 0 

    documento = [x.lower() for x in documento]

    for palavra in documento:
        sub = palavra.split(', ')
        lista_separada.append(sub)
        

    for elemento in lista_separada:
        if elemento[0][0] == 'a': 
            contador += 1

print(contador)