import datetime
t1=datetime.now().strftime('%H:%M:%S')
t2=datetime.now().strftime('%H:%M:%S')
def segundos_entre(t1, t2):
    t1s=(t1.hour*60*60+t1.minute*60+t1.second)
    t2s=(t2.hour*60*60+t2.minute*60+t2.second)
    delta=t1s-t2s
    return delta