def traduz(words, eng2port):
    palavras = []
    for word in words:
        for ing, port in eng2port.items():
            if word == ing:
                palavras.append(port)
    return palavras
    