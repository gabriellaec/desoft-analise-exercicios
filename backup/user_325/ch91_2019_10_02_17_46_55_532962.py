from string import ascii_lowercase
from collections import Counter

with open("palavras.txt") as f:
    print(Counter(letter for line in f 
                  for letter in line.lower() 
                  if letter in ascii_lowercase)
#esse programa conta todas as palavras, e consequentemente a letra "A" e "a"também