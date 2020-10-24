def preco(d):
    if d < 200:
        return d * 0.5
    elif d >= 200:
        return (d - 200) * 0.45 + 100
