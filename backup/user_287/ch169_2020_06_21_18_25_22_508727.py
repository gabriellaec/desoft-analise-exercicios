nome = True
fim = ['fim']
lista_usuarios = []
while nome:
    user = str(input('Usuario: '))
    if user in fim:
        nome = False
    else:        
        lista_usuarios.append(user) 
        
for i in range(len(lista_usuarios)):
    print(lista_usuarios[i])


      
        