with open("macacos-me-mordam.txt",'r') as macacos:
    conteudo = macacos.read()
   
tx=conteudo.split()
x=0
for i in tx:
    min = i.lower()
    if min == "banana":
        x+=1
print(x)
    

    