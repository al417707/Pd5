def szyfruj(tekst, kod):
    tekst_new = ''
    for i in tekst:
        if i in kod.keys():
            tekst_new += kod[i]
        else:
            tekst_new += i
    return tekst_new

print("Wybierz szyfr:")
d = input("1 -  GADERYPOLUKI, \n2 - POLITYKARENU, \n3 - niestandardowy ")
if d == '1':
    kod_str = 'GADERYPOLUKI'
if d == '2':
    kod_str = 'POLITYKARENU'
if d == '3':
    kod_str = input("podaj kod")

if len(kod_str)%2==1 or (len(set(kod_str)) != len(kod_str)):
    print('Zły kod')
else:
    kod_str = kod_str.lower()
    i=0
    kod = {}
    while i < len(kod_str):
        kod[kod_str[i]] = kod_str[i+1]
        kod[kod_str[i+1]] = kod_str[i]
        i+=2

try:
    if(kod):
        tekst = input("Podaj tekst ")
        tekst = tekst.lower()
        print(szyfruj(tekst, kod))
except:
    print('nie zadziała')