c=0
with open ("churras.txt","r") as arquivo:
    arquivo= arquivo.readlines()
    linha= arquivo.split(",")
    for i in linha:
        c+=float(i[1])*float(i[2])
print (c)
    