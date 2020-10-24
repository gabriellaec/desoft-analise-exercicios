with open("macacos-me-mordam.txt",'a') as arquivo:
	conteudo= arquivo.read()
soma=0
texto = conteudo.split()
for e in texto:
    maiusculo= conteudo.upper()
    if maiusculo== "BANANA":
       	soma+=1
print(soma)