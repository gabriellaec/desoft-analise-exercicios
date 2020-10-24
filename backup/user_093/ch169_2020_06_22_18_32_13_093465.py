login=input('login')
lista=[]
while l != 'fim':
    if not login in lista:
        lista.append(login)
    else:
        i=1
        while True:
            login2=logins+str(i)
            if not login2 in lista:
                lista.append(login2)
            i+=1
            
for nome in lista:
    print(lista)
    


           