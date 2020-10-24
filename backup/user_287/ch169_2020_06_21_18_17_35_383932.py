nome = True
fim = ['fim']
lista_usuarios = []
while nome:
    user = str(input('Usuario: '))
    if user in fim:
        nome = False
    else:        
        lista_usuarios.append(user) 
print(lista_usuarios(user))
      
        