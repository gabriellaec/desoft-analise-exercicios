maior_numero = 1
valor_atual = 2
contagem_de_termos = 1
maximo_de_termos = 0
guarda_valor_inicial = 0

while valor_atual < 1000:
    
    guarda_valor_inicial = valor_atual - 1    
    contagem_de_termos = 1
    
    while valor_atual != 1:
        
        contagem_de_termos += 1
        
        if valor_atual % 2 == 0:
           valor_atual = valor_atual/2
        
        else:
           valor_atual = 3*valor_atual + 1
        
    if maximo_de_termos < contagem_de_termos:
        maximo_de_termos = contagem_de_termos
        maior_numero = guarda_valor_inicial + 1
   
    valor_atual = guarda_valor_inicial + 2 

print (maior_numero)