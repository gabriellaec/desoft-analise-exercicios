with open ("texto.txt", "r") as arquivo:
    ler = arquivo.read()
    x = ler.split()
    print (len(x))