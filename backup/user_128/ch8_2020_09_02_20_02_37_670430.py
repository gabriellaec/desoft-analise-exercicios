def calcula_posicao(t, s0, v):
    s = s0 + (v * t)
    return s

resposta = calcula_posicao(20, 10, 15)
print(resposta)
