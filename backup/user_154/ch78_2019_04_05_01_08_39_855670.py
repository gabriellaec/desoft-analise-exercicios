import math

def calcula_tempo(dic):
    result = {}
    
    for key, value in dic.items():
        result[key] = math.sqrt(200/value)
    
    return result

dic = {}

while True:
    name = input("Nome")
    
    if name == "sair":
        break
    else:
        dic[name] = float(input("Aceleração"))

tempo = 0
vencedor = ""

for key, value in calcula_tempo(dic):
    if vencedor == "":
        tempo = value
        vencedor = key
    if value < tempo:
        tempo = value
        vencedor = key

print("O vencedor é {0} com tempo de conclusão de {1} s".format(vencedor, tempo))