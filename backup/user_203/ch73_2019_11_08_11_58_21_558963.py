def remove_vogais(string):
    i = 0
    while i < len(string):
        if string[i] == "a":
            del string[i]
		if string[i] == "e":
            del string[i]
		if string[i] == "i":
            del string[i]
		if string[i] == "o":
            del string[i]
		if string[i] == "u":
            del string[i]
		else:
            return string
        