def login_disponivel(login,listadelogins):
    lista=listadelogins
    listasemnumero = []
    numero='1,2,3,4,5,6,7,8,9'
    n=0
    for i in lista:
        listasemnumero.append(i.rstrip(numero))

    if login not in lista:
        return(login)
    else:
        n=listasemnumero.count(login)
        return(login+str(n))


listadelogins=[]
x='x'
while True:
    x=input("Qual o usuário?\n")
    if x == 'fim':
        break
    else:
        listadelogins.append(login_disponivel(x,listadelogins))
print (listadelogins)
