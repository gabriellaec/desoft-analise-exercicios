lista = []
quer_escrever = True
while quer_escrever:
    palavra = input('Você ainda quer escrever algo? ')
    if palavra == 'fim':
        quer_escrever = False
    else:
      lista.append(palavra)
n_elementos = 0
a = 'a'
A = 'A'
while n_elementos < len(lista):
    word = lista[n_elementos]
    if word[0]== a or word[0]== A:
        print(lista[n_elementos])
        n_elementos += 1
    else:
        n_elementos += 1