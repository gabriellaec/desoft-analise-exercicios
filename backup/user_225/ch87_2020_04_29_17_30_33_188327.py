with open("churras.txt","r") as arquivo:
    lista = []
    valor = 0
    for i in arquivo:
        linha = arquivo.readline()
        listaa = linha.split(',')
        a = int(listaa[1])
        b = int(lista[2])
        valor+= a*b
        print(valor)

   
    