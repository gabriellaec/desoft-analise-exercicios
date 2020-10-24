def primeiras_ocorrencias(string):
    dict = {}
    for i in range(0,(len(string)-1)):
        if string[i] not in dict:
            string[i] = b
            dict[string[i]] = i
    return dict