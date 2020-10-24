def idade(x):
    if x <= 11:
        return "crianca"
    elif x >= 12 or x <= 17:
        return "adolescente"
    else x >= 18:
        return "adulto"