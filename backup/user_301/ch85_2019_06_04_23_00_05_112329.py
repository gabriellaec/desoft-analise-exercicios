with open ("macacos-me-mordam.txt","r") as arquivo:
    texto = arquivo.read()
    lista = texto.split()
    i=0
    for e in lista:
        if (e[0] == "b" or e[0] == "B") and\
           (e[1] == "a" or e[0] == "A") and\
           (e[2] == "n" or e[2] == "N") and\
           (e[3] == "a" or e[3] == "A") and\
           (e[4] == "n" or e[4] == "N") and\
           (e[5] == "a" or e[5] == "A"):
              i+=1
print (i)
          