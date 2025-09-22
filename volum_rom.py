def les_inn_ikke_negativt_flyttall(variabelnavn):
    fortsetter = True
    while fortsetter:
        tall_str = input(f"Skriv inn {variabelnavn} til rommet: ")
        try:
            verdi = float(tall_str)
        except ValueError:
            verdi = -1
        if verdi < 0:
            print("Skriv inn et gyldig ikke-negativt flyttall. prøv på nytt.")
        else:
            fortsetter = False
    return verdi


lengde_meter = les_inn_ikke_negativt_flyttall("lengde")
bredde_meter = les_inn_ikke_negativt_flyttall("bredde")
hoyde_meter = les_inn_ikke_negativt_flyttall("høyde")
volum_kubikkmeter = lengde_meter*bredde_meter*hoyde_meter
print("Volumet ble", volum_kubikkmeter, " kubikkmeter")
