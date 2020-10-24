dicio={}
dicio2={}

naosair=True
while naosair==True:
    nome=input("Digite o nome")   
    if nome =="sair":
        naosair=False
    else:
        aceleracao=int(input("Digite a aceleracao"))
        dicio[nome]=aceleracao

for i in dicio.values():
    t=(200/i)**0.5
    for g in dicio:
        if dicio[g]=i:
            dicio2[g]=t
            
mini = min(dicio2, key=dicio2.get)
                           
for a in dicio2:
    if dicio2[a]==mini:
        print("O vencedor é {0} com tempo de conclusão de {1} s".format(a, mini))