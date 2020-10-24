from collections import Counter
    def conta_letra(string):
    [[x,l.count(x)] for x in set(l)]
    return dict((x,l.count(x) for x in set(l)))