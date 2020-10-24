nome = True
while nome:
    lista_usuarios = []
    user = str(input('Usuario: '))
    if user != 'fim':
        user = str(input('Usuario: '))
        lista_usuarios.append(user)    
    else:
        nome = False
        break
        
print(lista_usuarios)
      
        