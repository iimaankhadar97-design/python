#BMA calculator
def xisabi_bmi():
    culayska = float(input("soo gali culayskaga isoo KG: "))
    jogga = float(input("soo gali jogaaga oo meter ah: "))
    bmi = culayska / jogga**2
    if bmi < 18.5:
        print("misaankaga kordhi")
    elif 18.5 <= bmi < 24.9:
        print("misaankaagu waa caadi")
    elif 25 <= bmi < 29.9: 
        print("miisanka iska rid")
    else:
        print("culayskaagu aad buu u sareeyaa")
xisabi_bmi()        
