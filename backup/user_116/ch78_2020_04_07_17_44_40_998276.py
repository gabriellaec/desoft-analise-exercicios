def calcula_tempo(dicat):
    novodic={}
    for nome,ace in dicat.items():
        novodic[nome]=((200/ace)**(1/2))
    return novodic




n=str(input("digite um nome: "))
dicionario={}
listav=[]
diciresp={}
while n !=("sair"):
    if n not in dicionario:
        a=int(input("digite a aceleracao"))
        dicionario[n]=a
        n=str(input("digite outro nome: "))
    else:
        n=str(input("esse nome ja tem ,digite outro nome: "))

y=calcula_tempo(dicionario)
for va in y.values():
    listav.append(va)
for p,q in y.items():
    diciresp[q]=p
zmax=max(listav)
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(diciresp[zmax],zmax))