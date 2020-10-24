with open('texto.txt', 'r') as arquivo:
    ler = arquivo.read()
ler_l = ler.split()
tamanho = len(ler_l)
print(tamanho)