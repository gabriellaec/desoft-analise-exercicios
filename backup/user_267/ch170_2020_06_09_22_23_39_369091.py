
def apaga_repetidos(string):
    #esc = ''
    for i in range(len(string)):
        if string[i] == string[i-1]:
            string[i] = "*"
            #esc += "*"
        #else:
            #esc += string[i]
    return string
    #return esc

