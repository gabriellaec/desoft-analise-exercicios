def calcula_tempo(dic):
    final={}
    nomes=[]
    tempos=[]
    t=0
    i=0
    for x in dic.keys():
        nomes.append(x)
    for a in dic.values():
        t=10*(2**(1/2))/(a**(1/2))
        tempos.append(t)
    for y in nomes:
        final[y]=tempos[i]
        i=i+1
    return final
  
    
def vencedor(dic):
    lista_nomes=[]
    lista_tempo=[]
    for o in calcula_tempo(dic).keys():
        lista_nomes.append(o)
    for e in calcula_tempo(dic).values():
        lista_tempo.append(e)
    nome= lista_nomes[0]
    tempo= lista_tempo[0]
    for r in calcula_tempo(dic):
        if calcula_tempo(dic)[r] < tempo:
            tempo= calcula_tempo(dic)[r]
            nome= r
    h= 'O vencedor é {0} com tempo de conclusão de {1} s'.format(nome, tempo)
    return h


dic={}
Nome= input("Escolha um nome: ")

while Nome != 'sair':
    Aceleracao= float(input('Qual foi sua aceleração? '))
    dic[Nome]=Aceleracao
    Nome= input("Escolha um nome: ")
    



print(vencedor(dic))