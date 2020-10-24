def calcula_tempo(nada):
    dic = {}
    for atleta, aceleracao in nada.items():
        tempof = (200/aceleracao)**0.5
        dic[atleta] = tempof
    return dic

a = 0
compete = {}

while True:
    a = str(input("Digite o nome do atleta: "))
    if a != "sair":
        b = int(input("Digite a aceleracao do atleta: "))
    else:
        break
    compete[a] = b
    
atltemp  = calcula_tempo(compete)
amelhor = 10000000000000
tfinal = 10000000000000

for a, t in atltemp.items():
    if t < tfinal:
        tfinal = t
        amelhor = a
        
        

print("O vencedor é {} com tempo de conclusão de {} s".format(amelhor, tfinal))