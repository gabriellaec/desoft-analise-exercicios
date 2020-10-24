with open("macacos-me-mordam.txt","r") as arquivo:
    linhas=arquivo.readlines()
    palavra=linhas_nova.split()
    palavra2=palavra.lower()
    contador=0
    if "banana" in palavra2:
        contador+=1
print (contador)