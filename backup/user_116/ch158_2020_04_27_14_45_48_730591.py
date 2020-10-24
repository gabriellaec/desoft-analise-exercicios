with open("texto.txt","r") as arquivo:
    leitura=arquivo.read()
    lista=leitura.split()
    contador=len(lista)
print(contador)