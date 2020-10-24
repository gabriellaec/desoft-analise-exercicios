nome = str(input('Nome do mes: '))
meses=['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
i=0
while i < len(meses):
    i+=1
    if nome==meses[i]:
        i=i+1
        print(i)
    
    