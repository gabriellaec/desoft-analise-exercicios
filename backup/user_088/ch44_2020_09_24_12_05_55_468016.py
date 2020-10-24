nome_mes=['janeiro',' fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
i=0
numero_mes=[0]*11
pergunta_mes=input('qual o mes')
while(i<12):
        if(pergunta_mes==nome_mes[i]):
            print(numero_mes[i-1])
i+=1
         
           