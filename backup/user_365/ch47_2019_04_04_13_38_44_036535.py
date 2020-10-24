mes=int(input('n do mes'))
meses=['jan','fev','mar','abr','maio','jun','jul','ago','set','out','nov','dez']
i=0
while i<len(meses):
    if mes-1==i:
        print(meses[i])
    i+=1