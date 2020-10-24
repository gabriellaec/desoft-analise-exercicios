nome=input('Qual mês?')
mes=[0,'janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
t=1
while t<=12:
    if mes[t]!=nome:
        t+=1
    else:
        print('Mês {0}'.format(t))
        break
      

    
  