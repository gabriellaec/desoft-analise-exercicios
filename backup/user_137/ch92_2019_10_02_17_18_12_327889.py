def simplifica_dict(d):
    result = []
    for key in d.keys():
        result.append(d[key])
        result.append(key)
    return list(set(result))