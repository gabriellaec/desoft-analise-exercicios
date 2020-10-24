with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
contador=0 
conteudo.replace('\n',',')
conteudo.replace(' ',',')
conteudo.replace('	',',')
conteudo_lista=conteudo.split(',')
for e in conteudo_lista:
    e_maiusculo = e.upper()
    if e_maiusculo == 'BANANA':
        contador+=1 
print(contador)
    