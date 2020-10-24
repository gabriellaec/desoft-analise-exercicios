nome=input("Qual o nome do mês?")
ind = -1
i = 0

while i<len(meses):
    if meses[i]==nome:
        ind = i
i+=1
if ind==-1:
    print ("mês inválido")
    else:
        print (ind + 1)