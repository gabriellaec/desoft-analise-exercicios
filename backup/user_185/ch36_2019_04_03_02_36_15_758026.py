def eh_primo(número):
    if número%2 == 0 and número != 2:
        return False
    elif número == 0 or número == 1:
        return False
    elif número %3 == 0 and número != 3:
        return False
    elif número %5 == 0 and número != 5:
        return False
    elif número %7 == 0 and número != 7:
        return False
    else:
        return True