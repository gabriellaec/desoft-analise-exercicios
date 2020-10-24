def capitaliza(string):
    for i in range(len(string)):
        if i == 0:
            string[i] = string[i].upper()
    return string