def conta_bigramas(string):
    dic = dict()
    i = 1
    while i <= len(string):
        if '{0}{1}'.format(string[i-1], string[i]) in dic:
            dic['{0}{1}'.format(string[i-1], string[i])] += 1
            i += 1
        else:
            dic['{0}{1}'.format(string[i-1], string[i])] = 1
            i += 1
    return dic