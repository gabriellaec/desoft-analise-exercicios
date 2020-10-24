def junta_nome_sobrenome(nome,sobrenome):
juncao=[]
i=0
j=0
while(i<len(nome) and j<len(sobrenome)):
       juncao.append(nome[i],sobrenome[j])
          i+=1
              j+=1
    return juncao                 
    
    