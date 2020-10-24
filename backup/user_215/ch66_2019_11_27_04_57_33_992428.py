alfabeto_min = ["a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
alfabeto_mai = ["A", "B", "C", "D", "E", "F", "G", "H", 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

def capitaliza(string):
    i = 0
    while string[0] != alfabeto_min[i]:
        i += 1
        if string[0] == alfabeto_min[i]:
            string.replace(string[0], alfabeto_mai[i], 1)
    return string