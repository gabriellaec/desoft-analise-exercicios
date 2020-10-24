
from datetime import datetime
def segundos_entre(x,y):

    t1 = datetime.strptime(x, "%H:%M:%S")
    t2 = datetime.strptime(y, "%H:%M:%S")
    t2 - t1

    a = (t2 - t1).seconds

    return f'A diferença entre os horários {x} e {y} é: {a} segundos'

