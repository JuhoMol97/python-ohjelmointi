kalan_mitta = int(input("Minkä pituisen kuhan sait? "))
min_mitta = 37
if kalan_mitta < min_mitta:
    print(f"Kuha on alamittainen, laske se takaisin järveen. Kuha on {min_mitta - kalan_mitta}cm liian lyhyt.")
else:
    print(f"Kuha on tarpeeksi pitkä.")