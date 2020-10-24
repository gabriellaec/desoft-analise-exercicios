wordlist = []
wordlist_input = input("Palavra: ")
wordlist.append(wordlist_input)
while wordlist_input!="fim":
	wordlist_input = input("Palavra: ")
	wordlist.append(wordlist_input)

for i in range (len(wordlist)-1):
	firstletter = wordlist[i][0]
	if firstletter=='a':
		print (wordlist[i])