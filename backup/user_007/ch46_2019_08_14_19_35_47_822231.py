lista = []
palavra = 'inicio'
while palavra != 'fim':
    palavra = input()
    lista.append(palavra)
for nome in lista:
    if nome[0] == 'a':
        print(nome)