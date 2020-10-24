def calcula_tempo(dicionario):
    novo_dicionario={}
    for nomes, aceleracao in dicionario.items():
        novo_dicionario[nomes]=(200/aceleracao)**0.5
    return novo_dicionario


dicionario={}
ON=True
while ON:
    a=input()
    if a=="sair":
        break
    b=int(input())
    dicionario[a]=b
    
    
novodict=calcula_tempo(dicionario)

for nome, tempo in novodict.items():
    if tempo<a:
        x=tempo
       	y=nome