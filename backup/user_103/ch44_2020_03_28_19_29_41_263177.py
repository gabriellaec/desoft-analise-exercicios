a=input('Digite um mês')
i=0        
nome_do_mês=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
numero_do_mês=['1','2','3','4','5','6','7','8','9','10','11','12']
while a in nome_do_mês:
    nome_do_mês[i]=numero_do_mês[i]
    print(numero_do_mês[i])   
