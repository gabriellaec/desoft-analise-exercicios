with open("macacos-me-mordam.txt", 'r') as arquivo:
    conteudo=arquivo.read()
    conteudo=conteudo.lower()
    arroz=conteudo.split()
    
    banana=0
for i in arroz:
    
    if i == 'banana':
        banana=1+banana
print(banana)    
        