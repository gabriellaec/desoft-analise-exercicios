def remove_vogais(string):
    for word in string:      
    	if word == 'a' or 'e' or 'i' or 'o' or 'u':
        	string = string.replace(word, '')
    return string