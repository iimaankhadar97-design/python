import time 
def tiriye(ilbidhiqsi):
    while ilbidhiqsi:
        daq, ilbidh = divmod(ilbidhiqsi, 60)
        qabkawakhtiga = '{:02d}: {:02d}' .format(daq, ilbidh)
        print(qabkawakhtiga, end="\r")
        time.sleep(1)
        ilbidhiqsi -= 1
    print("wuu dhamaaday")
ilbidhiqsi = int(input("soo gali wkhtiga ilbidhiqsi ahaan"))        
tiriye(ilbidhiqsi)