def calcula_tempo(dic):
    saida={}
    for k,v in dic.items():
        saida[k] = ((200*v)**0.5)/v
    return saida
dic = {}
n = True
vencedor = ''
tempo=''
t = 10e5
while n:
    nome = input("Nome do atleta:")
    if nome == "sair":
        n = False
    else:
        aceleracao = int(input("Aceleracao do atleta:"))
        dic[nome] = aceleracao
saida = calcula_tempo(dic)
for at,tempo in saida.items():
    if tempo < t:
        t = tempo
        vencedor = at
print("O vencedor é {0} com tempo de conclusão {1}".format(vencedor,t))