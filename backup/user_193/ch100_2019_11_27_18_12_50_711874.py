login="Gabriel"
users=[]
while login!="fim":
    login=input("Digite seu login desejado: ")
    nome=login_disponivel(login,users)
    users.append(nome)
    print(nome)