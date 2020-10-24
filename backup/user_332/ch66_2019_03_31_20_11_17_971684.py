def capitaliza (palavra):
    cap = {
            "a":"A"
            "b":"B"
            "c":"C"
            "d":"D"
            "e":"E"
            "f":"F"
            "g":"G"
            "q":"Q"
            "w":"W"
            "r":"R"
            "t":"T"
            "y":"Y"
            "u":"U"
            "i":"I"
            "o":"O"
            "p":"P"
            "s":"S"
            "h":"H"
            "j":"J"
            "k":"K"
            'l':'L'
            'z':'Z'
            'x':'X'
            'v':'V"
            'n':'N'
            'm':'M'}
    
    palavra[0] = cap[palavra[0]]
    return(palavra)
    
print(capitaliza ("liso"))