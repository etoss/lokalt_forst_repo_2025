# Konstant
GRAVITASJON_PAA_JORDA = 9.8 # meter pr sekund i andre

def hastighet_i_fall(tid_sekunder):
    hastighet = tid_sekunder*GRAVITASJON_PAA_JORDA
    return hastighet


tid_sekunder = float(input("Tid: "))
hastigheten = hastighet_i_fall(tid_sekunder)
print(hastigheten)
