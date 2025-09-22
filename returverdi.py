def les_inn_ikke_negativt_flyttall(variabelnavn):
    tall_str = input(f"Skriv inn {variabelnavn}: ")
    verdi = float(tall_str)
    while verdi < 0:
        print("Tallet kan ikke være negativt. prøv på nytt.")
        tall_str = input(f"Skriv inn {variabelnavn}: ")
        verdi = float(tall_str)
    return verdi


def areal_rettvinklet_trekant(sidelengde_1, sidelengde_2):
    resultat = (sidelengde_1*sidelengde_2)/2
    return resultat


verdi = areal_rettvinklet_trekant(les_inn_ikke_negativt_flyttall("side 1"),
                                  les_inn_ikke_negativt_flyttall("side 2"))
print(verdi)
verdi = areal_rettvinklet_trekant(7, 8)
print(verdi)
verdi = areal_rettvinklet_trekant(9, 3)
print(verdi)
