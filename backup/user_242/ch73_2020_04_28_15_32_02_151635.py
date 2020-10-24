def remove_vogais(string):
    string_nova=[]
    i=0
    n = len(string)
    while i < n:
        if string [i] == 'a'or string[i] =='e'or string[i] == 'i'or string[i]=='o'or string[i] == 'u':
            del string[i]
        else:
            string_nova.append(string[i])
    return string_nova