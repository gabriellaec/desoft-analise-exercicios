def estritamente_crescente(fora_de_ordem):
    em_ordem = []
    em_ordem.append(fora_de_ordem[0])
    t = 0
    while t < (len(fora_de_ordem)-1):
        if fora_de_ordem[t+1] > fora_de_ordem[t]:
            em_ordem.append(fora_de_ordem[t+1])
        t += 1
    return em_ordem