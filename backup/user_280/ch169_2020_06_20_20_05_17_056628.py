def login_disponivel(string, lista):
    i = 0
    c = 0
    d = string
    j = len(lista[i])
    while i < len(lista):
        if d == lista[i]:
            c+=1
            d = d[0:len(string)] + str(c)
        i+=1
    return d

resposta = str(input('diga um login: '))
lista = []
while resposta != "fim":
    lista.append(login_disponivel(resposta, lista))
    resposta = str(input('diga um login: '))
for i in range(len(lista)):
    print(lista[i])
