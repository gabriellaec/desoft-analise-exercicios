def eh_crescente(n):
    for i in range(len(n)-1):
        for e in range(1, len(n)):
            if n[e] > n[i]:
                return True
            else:
                return False
   