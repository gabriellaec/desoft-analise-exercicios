def traduz(eng, eng2port):
    port = []
    for i in range (len(eng)):
        for eng[i] in eng2port.keys():
            word = eng2port[eng[i]]
            port.append(word)
    return port
            