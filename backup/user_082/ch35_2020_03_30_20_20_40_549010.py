i=0
soma=0
while i==0:
    pergunta_usuario= int(input('Digite numeros para serem somados '))
    if pergunta_usuario != 0:
        soma += pergunta_usuario
    if pergunta_usuario == 0:
        i+=1
print(soma)
        