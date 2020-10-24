def separa_trios(L):
    assert type(L) is list, "L is not a list"
    for i in range(0, len(L), 3):
        yield L[i:i+3]
    return L