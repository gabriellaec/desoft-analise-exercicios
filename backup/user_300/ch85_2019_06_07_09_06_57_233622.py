with open("macacos-me-mordam.txt", "r") as arq1:
    cont1 = arq1.read()
def countFreq(pat, txt): 
    M = len(pat) 
    N = len(txt) 
    res = 0
      
    # A loop to slide pat[] one by one  
    for i in range(N - M + 1): 
          
        # For current index i, check  
        # for pattern match  
        j = 0
        for j in range(M): 
            if (txt[i + j] != pat[j]): 
                break
  
        if (j == M - 1): 
            res += 1
            j = 0
    return res 
      
# Driver Code 
 
txt = cont1
pat = "BANANA"
print(countFreq(pat, txt)) 

