n=str(input("digite um nome: "))
dicionario={}
novodici={}
listav=[]
diciresp={}
while n !=("sair"):
    if n not in dicionario:
        a=int(input("digite a aceleracao"))
        dicionario[n]=a
        n=str(input("digite outro nome: "))
    else:
        n=str(input("esse nome ja tem ,digite outro nome: "))
for nome,ace in dicionario.items():
        novodici[nome]=((200/ace)**(1/2))
for v in novodici.values():
    listav.append(v)
for p,q in novodici.items():
    diciresp[q]=p
zmax=max(listav)
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(diciresp[zmax],zmax))