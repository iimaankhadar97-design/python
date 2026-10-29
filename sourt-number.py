def tiro_kalasooc():
    tiroyin = input("tiro soo geli: ").split()
    tiroyin = [int(tiro) for tiro in tiroyin]
    kalasooc = sorted(tiroyin)
    print(f"tirooyinka lakala soocay waa: {kalasooc}")
tiro_kalasooc()   
    