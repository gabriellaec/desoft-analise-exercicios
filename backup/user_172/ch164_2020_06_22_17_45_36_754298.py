def traduz(eng, eng2port):
    port = []
    for i in eng and eng2port.keys():
        word = eng2port[i]
        port.append(word)
    return port
            