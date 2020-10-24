def simplifica_dict(d):
    d_list = []
    for item in d:
        if item not in d_list:
            d_list.append(item)
        if d[item] not in d_list:
            d_list.append(d[item])
    return d_list