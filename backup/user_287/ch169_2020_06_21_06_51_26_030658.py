nome = True
while nome:
    lista_usuarios = []
    user = str(input('Usuario: '))
    if user == 'fim':
        nome = False
        break
    else:
        user = str(input('Usuario: '))
        lista_usuarios.append(user)
        
print(lista_usuarios)
      
        