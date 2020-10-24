def calcula_posicao(instante_t, posicao_inicial, velocidade):
    posicao = posicao_inicial + velocidade*instante_t
    print("A posição do objeto é: {0}".format(posicao))
t = float(input("Informe o instante desejado: "))
s0 = float(input("Informe a posição inicial: "))
v = float(input("Informe a velocidade do objeto: "))
calcula_posicao(t, s0, v)