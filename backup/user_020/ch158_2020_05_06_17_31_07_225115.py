with open ('texto.txt', 'r') as arquivo:
    x = arquivo.read()
    y = x.split()
print(len(y))