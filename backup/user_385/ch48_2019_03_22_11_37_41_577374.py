meses=['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
nome= input('nome do mes:')
ind=-1
i=0
while i<len(meses):
    if meses[i]==nome:
        ind=1
    i+=1    
if ind ==-1:
    print('mes invalido')
else:
    print(ind+1)     
    