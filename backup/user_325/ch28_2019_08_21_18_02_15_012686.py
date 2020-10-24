def velocidade(v):
    if v > 80:
        m = (v - 80) * 5
        return("voce foi multado")
    else:
        return("Não foi multado")
print(velocidade(88))