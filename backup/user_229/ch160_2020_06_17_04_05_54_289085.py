import math
diferenca = 0
resposta = 0
for i in range(0, 90):
    funcao = math.sin(i)
    bhaskara = (4*i*(180-i))/(40500-i*(180-i))
    
    if abs(funcao-bhaskara) > diferenca:
        diferenca = abs(funcao-bhaskara)
        resposta = i
        
print(resposta)