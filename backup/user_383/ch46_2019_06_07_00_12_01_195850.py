lista_vazia=[]
palavra = input('Qual palavra voce deseja add na lista?')
i = 0
while palavra != 'fim':
    lista_vazia.append(palavra)
    palavra = input('Qual palavra voce deseja add na lista?')
while i < len(lista_vazia):
    if lista_vazia[i][0] == 'a':
        print(lista_vazia[i])
    i+=1