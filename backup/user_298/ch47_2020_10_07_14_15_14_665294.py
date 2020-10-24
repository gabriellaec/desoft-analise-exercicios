def estritamente_crescente(fora_de_ordem):
    if len(fora_de_ordem) == 0:
        return fora_de_ordem
    em_ordem = [fora_de_ordem[0]]
    t = 1
    while t < len(fora_de_ordem):
        if fora_de_ordem[t] > em_ordem[-1] :
            em_ordem.append(fora_de_ordem[t])
        t += 1
    return em_ordem