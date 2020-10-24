with open('texto.txt','r') as arquivo:
    conteudo=arquivo.read()
    
h=conteudo.split()
print(len(h))