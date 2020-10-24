from datetime import datetime, time as datetime_time, timedelta

def segundos_entre(comeco, fim):
    if isinstance(comeco, datetime_time):
        assert isinstance(fim, datetime_time)
        comeco, fim = [datetime.combine(datetime.min, t) for t in [comeco, fim]]
    if comeco <= fim: 
        return fim - comeco
    else: 
        fim += timedelta(1) 
        assert fim > comeco
        return fim - comeco

for alcance in ['10:33:26-11:15:49', '23:55:00-00:25:00']:
    s, e = [datetime.strptime(t, '%H:%M:%S') for t in alcance.split('-')]
    print(segundos_entre(s, e))
    assert segundos_entre(s, e) == segundos_entre(s.time(), e.time())