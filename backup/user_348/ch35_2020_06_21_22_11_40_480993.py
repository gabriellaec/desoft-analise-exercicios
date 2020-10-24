# Define uma variável condicional
número = True 
# Define uma variável com o valor inicial da soma (0 pois não foi adicionado nada)
soma = 0
# Define a condição do loop (enquanto a variável condicional é True)
while número:
    # Define uma variável com a pergunta e a resposta do usuário
    resposta = float(input('digite um numero:'))
    # Se o usuário escolhe um número diferente de 0, continua a soma e volta para o início do loop
    if resposta != 0:
        soma = soma + resposta
        número = True 
    # Se o usuário digita 0, imprime o valor atual da soma e sai do loop
    else:
        número = False
        print(soma)