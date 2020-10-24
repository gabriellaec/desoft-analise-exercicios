with open ('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
maiusculo=conteudo.upper()
contador=0
if maiusculo == 'BANANA':
    contador+=1
print (contador)
        