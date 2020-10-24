def traduz(eng,eng2port):
    port = []
    for i in range(len(eng)):
        port.append(eng2port.get(eng[i]))
    return port