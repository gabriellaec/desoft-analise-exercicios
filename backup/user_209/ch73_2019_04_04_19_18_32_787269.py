def remove_vogais (palavra):
    palavrinha = ""
    for e in range(len(palavra)):
        if palavra [e] != "a" and palavra [e] != "e" and palavra [e] != "i" and palavra [e] != "o" and palavra [e] != "u":
            palavrinha += palavra [e]
    return palavrinha