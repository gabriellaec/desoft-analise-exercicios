def traduz(l, d):
    final = []
    for ing in l:
        for kv in d.items():
            if ing == kv[0]:
                final.append(kv[1])
    return final