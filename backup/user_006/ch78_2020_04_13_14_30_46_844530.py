dicio={}
dicio2={}

naosair=True
while naosair==True:
    nome=input("Digite o nome")   
        if nome =="sair":
            naosair=False
        else:
            aceleracao=int(input("Digite a aceleracao")
            dicio[nome]=aceleracao

for i in dicio.values():
    t=(200/i)**0.5
    for b in dicio:
        if dicio[b]==i:
            dicio2[b]=t
mini=dicio[0]
for i in dicio2.values():                         
    if i<mini:
        mini=i
                           
for i in dicio2:
    if dicio2[i]==mini:
        print("O vencedor é {0} com tempo de conclusão de {1} s".format(i, mini))