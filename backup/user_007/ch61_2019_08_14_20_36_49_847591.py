def eh_palindromo(strg):
    str_aux = strg[::-1]
    for i in range(len(strg)):
      if str_aux[i] != strg[i]:
        return False
    return True