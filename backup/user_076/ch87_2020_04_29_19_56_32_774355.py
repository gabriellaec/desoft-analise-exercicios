with open('churras.txt','r') as arquivo:
    lista_itens = arquivo.readlines()
    i=0
    valor=0
    while i <len(lista_itens):
        valor += lista_itens[i][1] * lista_itens[i][2]
        i+=1
        
print(valor)