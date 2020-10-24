import math
dic = {}
while True:
    resposta = input("Qual o nome do atleta? ")
    if resposta == "sair":
        break
    else:
        dec[resposta]=int(iput("Qual a aceletação do atleta? "))
        
for k,v in dic.items():
    dic[k]= math.sqrt(200/v)
        
t = list(dic.values())
atletas = list(dic.keys())
    
print ("O vencedor é {1} com o tempo de cancelamento de {0} segundos".format(min(t),atletas[t.index(min(t))]))