nome=input("Qual o nome do mês?")
i = 0
ind = -1
while i<len(meses):
    if meses[i]==nome:
        ind = i
i+=1
if ind=-1:
    print ("mês inválido")
    else:
        print (ind + 1)