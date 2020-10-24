with open('macacos-me-mordam.txt','r') as arquivo:
    novo = arquivo.read()
    novo = novo.lower()
    cont = novo.count('banana')
print(cont)
    