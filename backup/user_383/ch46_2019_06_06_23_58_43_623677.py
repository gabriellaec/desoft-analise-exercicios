lista_vazia=[]
palavra = input('Qual palavra voce deseja add na lista?')
while palavra != 'fim':
    lista_vazia.append(palavra)
    if palavra[0] == 'a':
        print(palavra)