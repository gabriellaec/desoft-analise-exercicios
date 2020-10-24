with open("macacos-me-mordam.txt",'r') as arquivo:
	conteudo=arquivo.read()
conteudoseparado=conteudo.split()
ocorrencias=0  
for i in conteudoseparado:
    x=i.lower()
    if x== "banana":
        ocorrencias+=1
print(ocorrencias)
    