def remove_vogais(string):
    for word in string:      
    	if word == 'a' or 'e' or 'i' or 'o' or 'u':
        	del(string[word])
    return string