def junta_nome_sobrenome(nome,sobrenome):
    i=0
    lista=[]
    while i < len(nome) and i<len(sobrenome):
      lista.append(nome[i] + ' '+ sobrenome[i])
      i+=1
    return lista
a=['maria','joao','andre']
b=['john','mario','dre']
print(junta_nome_sobrenome(a,b))