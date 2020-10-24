def estritamente_crescente(l):
    cresce = True
    i = 1
    while cresce:
        if l[i-1] < l[i]:
            cresce = True
            return True
        else:
            cresce = False
            return False
        