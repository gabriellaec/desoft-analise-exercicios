def separa_trios(nomes):
    new = []
    for i in range(0, len(nomes), 3):
        new.append(nomes[i:i+3])
    print(new)
    return new
        