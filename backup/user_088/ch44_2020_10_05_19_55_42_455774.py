nome_mes=['janeiro',' fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
pergunta_mes=input('qual o mes')
i=0
while(i<len(nome_mes)-1):
        if(pergunta_mes==nome_mes[i]):
            print(i+1)
            break      
        i+=1
         
           