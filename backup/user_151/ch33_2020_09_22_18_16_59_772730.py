def primos_entre(a, b):
    i = a
    j = 0
    while i<=b :
        if eh_primo(i):
            j = j + 1
        i = i + 1
    return j

