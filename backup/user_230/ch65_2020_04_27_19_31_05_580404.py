def capitaliza (string):
    primeira=string[0]
    maiuscula=primeira.upper()
    nova=string.replace("{0}", "{1}".format(primeira, maiuscula))
    return nova