from datetime import datetime

def xisaabi_dada():
    dhalashada = input("gormaad dhalaty (yyyy-mm-DD): ")
    dhalashada = datetime.strptime(dhalashada, "%Y-%m-%d")
    manta = datetime.today()
    dada = manta.year - dhalashada.year - ((manta.month, manta.day) < (dhalashada.month, dhalashada.day ))
    print(f"waxaad jirtaa {dada} sanadood")
xisaabi_dada()  
