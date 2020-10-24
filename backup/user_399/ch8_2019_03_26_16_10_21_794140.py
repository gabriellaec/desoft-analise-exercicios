def verifica_progressao(n):
    i=0
    while i < len(n):
        i += 1
        if n[i] - n[i-1] == n[i+1] - n[i] and n[i] / n[i-1] == n[i+1] / n[i]:
            return "AG"
        elif n[i] / n[i-1] != n[i+1] / n[i]:
            return "PA"
        elif n[i] - n[i-1] != n[i+1] - n[i]:
            return "PG"
        elif n[i] - n[i-1] != n[i+1] - n[i] and n[i] / n[i-1] != n[i+1] / n[i]:
            return "NA"