with open("dados.csv","r") as arquivo:
    conteudo=arquivo.open()
a=conteudo.split()
nova=[]

for i in range(len(a)):
    if a[i]==",":
        a[i]="\t"
