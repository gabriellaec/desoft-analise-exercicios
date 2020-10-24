def remove_vogais(string):
    for i in range(len(string)):
        if string[i] == "a":
            string = string.replace(string[i],"")
    return string