lista = []
quer_escrever = True
while quer_escrever:
    palavra = input('Você ainda quer escrever algo?')
    if palavra == 'fim':
        quer_escrever = False
    else:
      lista.append(palavra)
n_elementos = 0
while n_elementos < len(lista):
    if palavra[0]!= 'a' or palavra[0]!='A':
        del(lista[n_elementos])
    else:
        print(lista[n_elementos])
        n_elementos += 1