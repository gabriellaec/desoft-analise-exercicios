nome = True
fim = ['fim']
lista_usuarios = []
while nome:
    user = str(input('Usuario: '))
    if user in fim:
        nome = False
    else:        
        lista_usuarios.append(user) 
print(lista_usuarios[0])
print(lista_usuarios[1])
print(lista_usuarios[2])
print(lista_usuarios[3],'1')

      
        