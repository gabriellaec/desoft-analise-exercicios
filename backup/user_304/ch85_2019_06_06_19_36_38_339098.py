with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    maiusculo=conteudo.upper()
    conta_banana=maiusculo.split()
    
contador=0
for e in conta_banana:
    if e == 'BANANA':
        contador+=1
print (contador)
        