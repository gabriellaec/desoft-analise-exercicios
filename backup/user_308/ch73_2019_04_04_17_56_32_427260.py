def remove_vogais(palobras):
    palavreras=""
    for e in range(len(palobras)):
        if palobras[e]!="a" and palobras[e]!="e" and palobras[e]!="i"  and palobras[e]!="o" and palobras[e]!="u":
            palavreras+=palobras[e]
    return palavreras