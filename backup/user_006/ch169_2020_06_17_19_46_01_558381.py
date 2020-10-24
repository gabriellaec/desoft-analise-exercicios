def login_disponivel(loginori, lista):
    i=0
    e=1
    login=loginori
    while i<len(lista):
        if login not in lista:
            return login
        else:
            login=loginori+str(e)
        e=e+1
        i=i+1   

lista=[]
login=""
while login!="fim":
    login=input("Digite um login:")
    prox=login_disponivel(login, lista)
    lista.append(prox)
for i in lista:
    print(i)