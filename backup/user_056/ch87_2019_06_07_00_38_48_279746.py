with open ("churras.txt", "r") as arquivo:
    conteudo=arquivo.read()
    
total=0
for linha in conteudo:
    lista=linha.split(",")
    total+=lista[1]*lista[2]

print(total)
    
    
    