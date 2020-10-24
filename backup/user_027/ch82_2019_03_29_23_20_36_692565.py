def primeiras_ocorrencias(x):
    watashi_wa = {}
    for i in x:
        if x.index(i) <= x.find(i):
            watashi_wa[i] = x.index(i)
    return watashi_wa