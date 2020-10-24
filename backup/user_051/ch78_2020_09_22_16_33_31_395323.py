#t=(200/a)**0,5
def calcula_tempo(dic_a):
    lista_nomes=list(dic_a.keys())
    lista_aceleracao=list(dic_a.values())
    lista_tempo=[]
    for a in lista_aceleracao:
        t=(200/a)**(1/2)
        lista_tempo.append(t)
    dicionario=dict(zip(lista_nomes,lista_tempo))
    return dicionario
#@#@#@#@#@#@#@
dic_a={}
sair='sair'
while True:
    competidores=input('Os competidores são: ')
    if competidores == sair:
        break
    acel=float(input('Qual é a aceleração deste copetidor? '))
    dic_a[competidores]=acel
dic_tempo=calcula_tempo(dic_a)
menor=1000000
for i in list(dic_tempo.values()):
    if i < menor:
        menor=i
for competidor,tempo in dic_tempo.items():
    if tempo == menor:
        print('O vencedor é', competidor,'com tempo de conclusão de', tempo,'s' )