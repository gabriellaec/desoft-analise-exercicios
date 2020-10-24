def remove_vogais(string):
    string = " "
    string2 = " "
    for e in range(len(string)):
        if string[e] != "aeiou":
            string2 += string[e]