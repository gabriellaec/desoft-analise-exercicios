with open('churras.txt','r') as arquivo:
    lista_linhas = arquivo.readlines()
    valor=0
    for i in lista_linhas:
        i.split(',')
        valor += float(i[1]) * float(i[2])
        
print(valor)