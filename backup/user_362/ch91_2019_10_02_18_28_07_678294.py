with open ("palavras.txt","r") as arquivo:
    conteudo=arquivo.read()
    sem_mai=conteudo.lower()

    
palavra=sem_mai.split()
#print(palavra)

contador=0
CONTADOR=0
for i in palavra:
    if i[0]=="a":
        contador+=1
print (contador)