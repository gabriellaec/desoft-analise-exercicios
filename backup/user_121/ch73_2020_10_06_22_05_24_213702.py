def remove_vogais(string):
    i=0
    while i<len(string):
        if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
            string[i].replace('a','')
            string[i].replace('e','')
            string[i].replace('i','')
            string[i].replace('o','')
            string[i].replace('u','')
        i+=1
    return string