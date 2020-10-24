valor_casa = float(input())
salario = float(input())
tempo_pagamento = float(input())

valor_pretacao = valor_casa/(12*(tempo_pagamento))

if (valor_pretacao) >= (0.3*salario):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')