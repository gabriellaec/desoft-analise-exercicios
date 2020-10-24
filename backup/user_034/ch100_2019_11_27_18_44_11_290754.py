a = (int(input("Digite um login")))
j=[]
o="fim"
while a != o:
    j.append(a)
    if a == j:
        def login_disponivel(login,lista):
            list = ["1,2,3,4,5,6,7,8,9"]
            i=0
            if login not in lista:
                print("Login Disponivel")
                i=0
            elif login in lista:
                while login in lista:
                    print ("login indisponivel")
                    login = login + list[i]
                    i+=1
            return login
    else:
        print(j)
        