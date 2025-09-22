# Lager en funksjon med tre parametere og med standardverdier for alle tre
def ascii_firkant(bredde=3, hoyde=4, tegn="*"):
    for j in range(hoyde):
        for i in range(bredde):
            print(tegn, end="")
        print()


# Kaller funksjonen uten parametere, bruker da standardverdiene for alle tre parametrene
ascii_firkant()

# Kaller funksjonen med et vanlig argument, som blir gitt til den første parameteren "bredde", samt
# et navngitt argument.
ascii_firkant(5, tegn="%")

# Kaller funksjonen med alle tre argumentene oppgitt
ascii_firkant(3, 4, "#")
bredde_firkant = int(input("Bredde: "))
hoyde_firkant = int(input("Høyde: "))

# Kaller funksjonen med to navngitte argumenter, høyde og bredde.
ascii_firkant(hoyde=hoyde_firkant,  bredde=bredde_firkant)

ascii_firkant(5, 8, "-")
