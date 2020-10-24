with open("macacos-me-mordam.txt","r") as arquivo:
    linhas=arquivo.readlines()
    palavra=linhas.join()
    palavra2=palavra.split()
    palavra3=palavra.lower()
    contador=0
    if "banana" in palavra3:
        contador+=1
print (contador)