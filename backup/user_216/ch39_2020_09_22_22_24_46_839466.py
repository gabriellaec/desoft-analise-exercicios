numero_operacional = 1
numero = 1
termos = 1
termos_resposta = 2
resposta = 1

while numero < 1000:
    numero_operacional = numero
    while numero_operacional != 1:
        if numero_operacional %2 == 0:
            numero_operacional = numero_operacional/2
            termos += 1
        else:
            numero_operacional = numero_operacional * 3 + 1
            termos += 1
    if termos_resposta < termos:
        termos_resposta = termos
        resposta = numero
    numero += 1
    termos = 1

print(resposta)