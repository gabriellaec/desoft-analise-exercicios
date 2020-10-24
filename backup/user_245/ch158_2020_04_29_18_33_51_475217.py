with open('texto.txt','r') as texto:
    b = texto.read()
    a = b.split()
print(len(a))