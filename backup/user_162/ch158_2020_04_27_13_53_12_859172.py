with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    a = texto.split()
    count = len(a)
    
print(count)