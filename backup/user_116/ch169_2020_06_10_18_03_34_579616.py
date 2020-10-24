def login_disponivel(nome,lista):
    a=len(nome)
    contador=0
    for ele in lista:
        if ele[:a]==nome:
            contador+=1
    contador=str(contador)
    if contador=="0":
        return nome 
    else :
        return nome+contador
lista=[]
rsp=str(input('nome'))
while rsp!="fim":
    a=login_disponivel(rsp,lista)
    lista.append(a)

    rsp=str(input('nome'))
for el in lista:
    print(el)