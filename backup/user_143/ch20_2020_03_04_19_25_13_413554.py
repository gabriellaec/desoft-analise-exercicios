# Pergunta quantos km
km= float(input('quantos km:'))
def P(qts_km):
    if qts_km <= 200:
        y=qts_km*0.5
        return y
    else:
        y=qts_km*0.5 + (qts_km-200)*0.45
        return y
y = P(km)
print (y)