def PiWallis(n):

    numerator = 2.0
    denominator = 1.0
    pi = 1.0

    for i in range(1, n + 1):
        pi*= (numerator / denominator)
        if (i%2) == 1:
            denominator+= 2.0
        else:
            numerator+= 2.0

    pi*= 2.0

    return pi