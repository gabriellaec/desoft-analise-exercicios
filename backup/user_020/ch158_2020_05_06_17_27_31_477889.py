with open ('texto.txt', 'r') as arquivo:
    x = arquivo.readlines()
    y = x.split()
print(len(y))