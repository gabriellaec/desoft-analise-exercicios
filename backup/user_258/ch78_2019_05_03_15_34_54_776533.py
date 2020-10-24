def calcula_tempo(atletas):
    dic={}
    for e,v in atletas.items():
        dic[e]=(200/v)**0.5
    return dic

atletas={}
fim=False
while fim==False:
    nome=input('Qual o nome do atleta? ')
    if nome!='sair':
        aceleracao=float(input('Qual a aceleração do atleta? '))
        atletas[nome]=aceleracao
    else:
        fim=True
atletas_com_tempo=calcula_tempo(atletas)
menor=[]
nome=[]
for k,v in atletas_com_tempo.items():
    menor.append(v)
    nome.append(k)
Menor=min(menor)
i=0
while i<len(menor):
    if menor[i]==Menor:
        i=i
        break
    else:
        i+=1
Nome=nome[i]
print("O vencedor é {0} com tempo de conclusão de {1} s".format(Nome,Menor))

      
    

        
    


   
        
    
    
    