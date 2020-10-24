with open ("churras.txt","r") as arquivo:
    conteudo=arquivo.read()

linhas=conteudo.split('')
total=0
for l in linhas:
    colunas=l.split(",")
    soma=float(colunas[1])*float(colunas[2])
    total=total+soma
print(total)
    
    