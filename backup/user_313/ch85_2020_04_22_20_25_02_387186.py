with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()
    palavra = []
    for i in conteudo:
        x = i.split(' ')
        palavra += x
        
    
    
lista = list()

for i in palavra:
    a = i.strip()
    
    x = a.lower()
    
    lista.append(x)

cont = 0
for i in lista:
    
    if i == "banana":
        
        cont += 1
        
print(cont)