def apaga_repetido(str):
      lista = []
      newStr = “”
      i = 0
      while i < len(str):
            if str[i] in lista:
                 newStr = newStr + “*”
            else: 
                 newStr = newStr + str[i]
                 lista.append(str[i])
            i += 1
      return newStr