with open('churras.txt', 'r') as arquivo:
    valor=0
    for linha in arquivo:
        lista=linha.split(',')
        a=int(lista[1])
        b=float(lista[2])
        valor+=a*b
        print(valor)

