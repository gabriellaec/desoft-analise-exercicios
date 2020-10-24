c=0
with open ("churras.txt","r") as arquivo:
    arquivo= arquivo.readlines()
    for linha in arquivo:
        l=linha.split(",")
        c+=float(l[1])*float(l[2])
print (c)
    