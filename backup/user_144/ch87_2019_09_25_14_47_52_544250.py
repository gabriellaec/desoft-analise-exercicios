with open("churras.txt","r",encoding = "utf8") as arquivo:
    linhas = arquivo.readlines()

lista_total = []
for i in range(len(linhas)):
    lista_total.append(linhas[i].split(","))
    
print(lista_total)
        
custo = 0
for i in range(len(lista_total)):
    custo += int(lista_total[i][1]) * float(lista_total[i][2])

print(custo)