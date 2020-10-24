def traduz (lista, eng2port):
    port = []
    for l in lista:
        if l in eng2port.keys():
            port.append(eng2port[l])
    return port