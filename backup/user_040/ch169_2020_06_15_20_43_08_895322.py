def login_disponivel(nome, lista):
    numero  = 1
    for login in lista:
        if nome not in lista:
            return nome
        else:
            while nome in lista:
                if nome + str(numero) in lista:
                    numero += 1
                else:
                    return nome + str(numero)

nome = input("Qual o seu nome? ")
lista_nomes = []

while nome != "fim":
    nome = login_disponivel(nome, lista_nomes)
    lista_nomes.append(nome)
    nome = input("Qual o seu nome? ")

for x in lista_nomes:
    print (x)