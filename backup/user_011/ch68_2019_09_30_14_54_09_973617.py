def separa_trios(nomes):
    i = 3
    trios = []
    if len(nomes)%3 == 0:
        while i <= len(nomes):
            trio = nomes[0:i:1]
            trios.append(trio)
            i+=3
        return trios
    elif len(nomes) == 1 or len(nomes) == 2:
        return [nomes]    
    elif len(nomes)%3 == 2:
        while i <= len(nomes) - 2:
            trio = nomes[0:i:1]
            trios.append(trio)
            i+=3
        trios.append(nomes[-1:-3:-1])
        return trios
    else:
        while i <= len(nomes) - 1:
            trio = nomes[0:i:1]
            trios.append(trio)
            i+=3
        trios.append(nomes[-1])
        return trios
            