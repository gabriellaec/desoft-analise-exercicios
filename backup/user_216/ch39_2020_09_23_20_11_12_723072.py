numero_operacional = 1
numero = 1
termos_teste = 1
termos_resposta = 2
resposta = 1

while numero < 1000:
    numero_operacional = numero
    while numero_operacional != 1:
        if numero_operacional %2 == 0:
            numero_operacional = numero_operacional/2
            termos_teste += 1
        else:
            numero_operacional = numero_operacional * 3 + 1
            termos_teste += 1
    if termos_resposta < termos_teste:
        termos_resposta = termos_teste
        resposta = numero
    numero += 1
    termos_teste = 1
print(resposta)