def traduz(eng, eng2port):
    port = []
    i=0
    while i < len(eng):
        if eng[i] in eng2port.keys():
            word = eng2port[eng[i]]
            port.append(word)
        i+=1
    return port
            