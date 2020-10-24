with open("macacos-me-mordam.txt","r") as arquivo:
    linhas=arquivo.readlines()
    linhas_nova=linhas.lower()
    palavra=linhas_nova.split()
    contador=0
    if "banana" in palavra:
        contador+=1
print linhas_nova