with open('churras.txt','r') as arquivo:
    lista_linhas = arquivo.readlines()
    valor=0
    for i in lista_linhas:
        lista = i.split(',')
        valor += float(lista[1]) * float(lista[2])
        
print(valor)