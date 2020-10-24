Brasil = {'SP':{'SP':21571281,'Campinas':3224443},'MG':{'BH':2385639,'Uber': 611903}}

sumValue1 = sum(d['SP'] for d in Brasil.values() if d) 
sumValue2 = sum(d['BH'] for d in Brasil.values() if d) 
  
print(sumValue1) 
print(sumValue2) 