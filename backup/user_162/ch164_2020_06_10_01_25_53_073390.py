def traduz(lis, dic):
    traducao = []
    for eng in lis:
        for eng1, port in dic.items():
            if eng == eng1:
                traducao.append(port)
    return traducao