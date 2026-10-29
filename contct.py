contact = {}
def kudar_contact (magac,tell):
    contact[magac] = tell
    print(f"waa lagau daray {magac}")
def hubi_contact():
    if contact:
        print("\n listiga dadka")
        for magac, tell in contact.items():
            print(f"{magac}: {tell}")
    else:
        print("ma jiro magacan")
while True:
    print("\n 1. qof ku soo dar")
    print(" 2. hubi qofka ")
    print(" 3. ka bax")
    Doorosho = input("Dooro 1, 2, 3")
    if Doorosho == '1':
        magac = input("Geli magaca qofka ")
        tell = input("Geli telephonka qofka")
        kudar_contact( magac, tell)
    elif Doorosho == '2':
        hubi_contact()
    elif Doorosho == '3':
        print("ka bax")   
        break
    else:
        print("wax khaldan ayaad dawatay")                     
                