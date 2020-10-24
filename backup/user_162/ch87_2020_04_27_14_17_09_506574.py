with open('churras.txt', 'r') as arquivo:
    texto = arquivo.readlines()
    valor = 0
    
    for i in texto:
        i = i.split(",")
        valor += float(i[1])*float(i[2][:-1])
print(valor)