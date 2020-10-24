with open('texto.txt', 'r') as arquivo:
    ler = arquivo.read()
    split = ler.split()
    print(len(split)