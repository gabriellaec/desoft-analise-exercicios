running=True
lista=[]
while running:
    login=input('qual o login')
    if login != 'fim':
        lista.append(login)

print(login_disponivel(login,lista))
        