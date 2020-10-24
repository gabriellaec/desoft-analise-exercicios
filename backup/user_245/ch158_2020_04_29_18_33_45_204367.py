with open('text.txt','r') as texto:
    b = texto.read()
    a = b.split()
print(len(a))