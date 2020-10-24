def calcula_tempo(d1):
    d2={}
    for atleta, acelerac in d1.items():
        t = (200/acelerac)**0.5
        d2[atleta]= t
    return d2

nome=input("nome: ")
d ={}
while nome != "sair":
    ac = int(input("aceleracao: "))
    d[nome]=ac
    nome=input("nome: ")
d_t=calcula_tempo(d)
mais_rapido =''
menor=10000000000
for atleta, tempo in d_t.items():
    if tempo<menor:
        menor=tempo
        mais_rapido=atleta
print('O vencedor é {} com tempo de conclusão de {} s'.format(mais_rapido, menor))
        
    

