def hubi_prime():
    tiro = int(input("soo gali tiro: "))
    if tiro <= 1:
        print(f"{tiro} ma ahan tiro mutuxan")
    else :
        for t in range(2, int(tiro ** 0.5) + 1):
            if tiro % t == 0:
                print(f"{tiro} ma aham tiro mutuxan")
                break
        else:
            print(f"{tiro} waa tiro mutuxan") 
hubi_prime()               