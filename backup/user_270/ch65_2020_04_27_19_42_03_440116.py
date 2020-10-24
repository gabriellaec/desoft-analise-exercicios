def capitaliza(s):
    s_up = s[0].upper()
    del s[0]
    s_new = s_up + s
    return s_new