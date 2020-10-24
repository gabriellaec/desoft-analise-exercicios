c=0
with open ("churras.txt","r") as arquivo:
    arquivo= arquivo.readlines()
    linha= arquivo.split(",")
    for i in linha:
        c+=float(linha[1])*float(linha[2])
print (c)
    