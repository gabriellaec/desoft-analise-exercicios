with open("texto.txt","r") as arquivo:
    ler = arquivo.read()
    lista = ler.split(",")
    
    print(len(lista))