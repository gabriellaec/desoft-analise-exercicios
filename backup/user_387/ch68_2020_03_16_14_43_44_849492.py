def separa_trios(a):
    chunks = [a[x:x+3] for x in range(0, len(a), 3)]
    return chunks
