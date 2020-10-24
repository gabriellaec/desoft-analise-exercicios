def capitaliza(T):
    first_ord = ord(T[0])
    if not (ord_A <= first_ord <= ord_Z):
        T = chr(first_ord - 32) + T[1:]
    return T