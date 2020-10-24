def remove_vogais(str):
    for i in str:
        if i == 'a' or 'e' or 'i' or 'o' or 'u':
            str.replace(i, "")
    return str        