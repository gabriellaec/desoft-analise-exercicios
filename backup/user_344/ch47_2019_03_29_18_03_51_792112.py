p=int(input('Qual numero do mes? '))
mes=['jan','fev','mar','abr','jun','jul','agt','sep','out','nov','dez']
i=0
while i<len(mes):
    i+=1
    if mes[i]== p:
        print(mes[i])