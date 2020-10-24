with open("churras.txt","r") as arquivo:
    valor = 0
    for linha in arquivo:
        listaa = linha.split(',')
        a = int(listaa[1])
        b = float(listaa[2])
        valor+= a*b
        print(valor)