sukupuoli = input("Anna biologinen sukupuolesi(M/N): ")
hemoglobiiniarvo = int(input("Anna hemoglobiiniarvosi: "))

if sukupuoli == "M":
    if hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvosi on korkea")
    elif 134 < hemoglobiiniarvo < 195:
        print("Hemoglobiiniarvosi on normaali")
    elif hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi on alhainen")
elif sukupuoli == "N":
    if hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvosi on korkea")
    elif 117 < hemoglobiiniarvo < 175:
        print("Hemoglobiiniarvosi on normaali")
    elif hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi on alhainen")
else:
    print("Virheellinen arvo")