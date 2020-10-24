def primeiras_ocorrencias (string):
    dic = {}
    for c in string:
        for i in range(len(string)):
            if c == string[i]:
                if not c in dic:
                    dic[c] = string[i]
    return dic