def conta_bigramas(string):
    dic = dict()
    i = 0
    while i <= len(string):
        if '{0}{1}'.format(string[i], string[i+1]) in dic:
            dic['{0}{1}'.format(string[i], string[i+1])] += 1
            i += 1
        else:
            dic['{0}{1}'.format(string[i], string[i+1])] = 1
            i += 1
    return dic