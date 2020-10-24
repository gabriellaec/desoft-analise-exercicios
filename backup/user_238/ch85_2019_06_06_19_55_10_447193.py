with open ("macacos-me-mordam.txt","r") as f:
    n=0
    linhas=f.read()
    linhas=linhas.lower()
    palavra=linhas.split()
for p in palavra:
            if p == "banana":
           		 n+=1
print(n)