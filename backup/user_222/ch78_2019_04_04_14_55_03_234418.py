nome=input('insira o nome')
dicionario={}
while nome!='sair':
    aceleracao=input('insira a aceleração')
    dicionario[nome]=aceleracao
def calcula_tempo(dicionario):
    tempo_conclusao=0
    Sf=100
    dicionario2={}
    for k,v in dicionario.items():
        tempo_conclusao=((2*Sf)/v)**(1/2)
        dicionario2[k]=tempo_conclusao
    for k,v in dicionario2.items():
        menor=-1
        nome=''
        menor_de_todos=0
        if v>menor:
            menor=v
        else:
            menor_de_todos=v
            nome=k
    return (nome,menor_de_todos)
print('o vencedor é {0} com tempo de conclusao de {1}s'.format(calcula_tempo(dicionario))
      