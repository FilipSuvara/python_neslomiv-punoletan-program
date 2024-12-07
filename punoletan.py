try:
    godine = int(input("Koliko imas godina?"))
    if godine <= 0:
        print("neispravan iznos")
    else:
        if godine > 122:
            print("druze nema sanse da imas toliko godina")
        else:
            if godine <18:
                print("maloletan")
            else:
                print("punoletan")
except:
    print("error")