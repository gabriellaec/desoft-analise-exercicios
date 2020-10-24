def capitaliza(string):
    cap = []
    for i in range(len(string)):
        cap.append(string[i].lower())
    y = ''.join(cap)
    z = cap[0].upper()
    return z