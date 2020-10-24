def calcula_tempo(D):
    C={}
    for nomes,aceleracao in D.items():
        a=aceleracao
        t=(200/a)**0.5
        C[nomes]=t
    return C

D={}
atletas=input("Qual o atleta?")
while atletas!="sair":
    aceleracao=float(input("Qual a aceleração?"))
    D[atletas]=aceleracao
    atletas=input("Qual o atleta?")
print(D)
h=calcula_tempo(D)
print(h)
menor_tempo=5000000000
campeao=" "
for nomes,tempo in h.items():
    if h[nomes]<menor_tempo:
        menor_tempo=h[nomes]
        print(menor_tempo)
        campeao=nomes
print("O vencedor é {0} com tempo de conclusão de {1} s".format(campeao,menor_tempo))