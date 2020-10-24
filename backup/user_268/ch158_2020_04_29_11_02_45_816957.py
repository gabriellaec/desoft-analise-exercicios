def contap(sla):
    with open(sla, "r") as arq:
        cont = arq.read()
        palavras = cont.split()
        return len(palavras)
