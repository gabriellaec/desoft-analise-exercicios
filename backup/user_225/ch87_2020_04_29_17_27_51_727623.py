with open("churras.txt","r") as arquivo:
    lista = []
    for i in arquivo:
        linha = arquivo.readline()
        listaa = linha.split(',')
        valor += listaa[1]*listaa[2]
    print(valor)
   
    