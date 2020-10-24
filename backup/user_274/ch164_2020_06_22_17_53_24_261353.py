def traduz(ing, eng2port):
    port = []
    for i in ing:
        if i in eng2port:
            port.append(eng2port[i])
    return port