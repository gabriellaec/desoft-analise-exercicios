def login_disponivel(string, lista):
    i = 0
    j = len(string) 
    c = 0
    d = string
    while i < len(lista):
        if string == lista[i][0:j]:
            c += 1
            d = string + str(c)
        i += 1  
    return d
resposta = str(input('diga um login: '))
lista = []
while resposta != "fim":
    print('{}'.format(login_disponivel(resposta, lista)))
    lista.append(login_disponivel(resposta, lista))
    resposta = str(input('diga um login: '))