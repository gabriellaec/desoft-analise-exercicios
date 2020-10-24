arquivo = open('churras.txt','r')
lista = arquivo.readlines()
arquivo.close()
valor = 0
for linha in lista:
    celulas = linha.split(',')
    valor += int(celulas[1]) * float(celulas[2])
print(valor)
    
    