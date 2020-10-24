def login_disponivel(nome, lista):
    i = 1
    if nome in lista:
        for n in lista:
            if "{}{}".format(nome, i) not in lista:
                return "{}{}".format(nome,i)
            i += 1

    
    else:
        return nome

lista_nomes = []
a = str(input(""))
lista_nomes.append(a)
while a != "fim":
    a = str(input(""))
    lista_nomes.append(login_disponivel(a, lista_nomes))

for i in lista_nomes:
    print(i)

