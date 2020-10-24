palavras=[]
texto=input(str("Palavra desejada: "))
palavras.append(texto)
while texto!= "fim":
    texto=input(str("Palavra desejada: "))
    palavras.append(texto)
numeropalavras=len(palavras)
contador=0
while contador<numeropalavras:
    p=palavras[contador]
    if p[0]=="a":
        print (p)
    contador+=1