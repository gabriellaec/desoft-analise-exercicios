inicial = int(input("Qual o deposito inicial:?"))
mensal = int(input("Qual o deposito mensal:?"))
taxa = float(input("Qual a taxa de juros:?"))
taxa2 = taxa + 1
i = 0
if i > 0:
    juros = inicial * taxa2
    total = inicial + mensal + juros
    i = i + 1
    while i < 24:
        total = (total + mensal) * taxa2
        final = total - (inical + 23 * mensal)
        i = i + 1
        
