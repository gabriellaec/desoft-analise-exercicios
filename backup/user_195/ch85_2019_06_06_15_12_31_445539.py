with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo_novo=str(conteudo)
contador=0 
conteudo_novo=conteudo_novo.replace('\n',',')
conteudo_novo=conteudo_novo.replace(' ',',')
conteudo_novo=conteudo_novo.replace('	',',')
conteudo_lista=conteudo_novo.split(',')
for e in conteudo_lista:
    e_maiusculo = e.upper()
    if e_maiusculo == 'BANANA':
        contador+=1 
print(contador)