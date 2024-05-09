import os
import time

ertekeles = []
def main():
    os.system("cls")
    print("""A történetünk a péceli katolikus iskolában játszódik.
A főhősök a diákok akiket a híres neves fortnine player Erika néni tart rettegésben az órákon.\nAki ezeken kívül egy kémia tanár.
\n\n-----\n\n A feladatod az lesz hogy megmentsed a diákokat.""")
    
    tov = input("Tovább (t) \|/ Kilépés(k): ")
    if tov == "t":
        kuldi1()
    if tov == "k":
        pass

def kuldi1():
    print("\n\n\n")
    print("12:00 :: A diákok bemennek az órára.")
    time.sleep(3)
    print("Erika kéri hogy a diákok alljanak föl.")
    time.sleep(0.8)
    q1 = input("Mit teszel?\n    Felállsz(1)\n    maradsz ülve(2)\n>>>")
    if q1 == "1":
        print("minden megy tovább... A hetes jelent.\n")
        time.sleep(0.7)
        print("A diákok leülnek és Erika kinyitja a könyvet")
        time.sleep(1)
        print("Erika bemegy a szertárba...")
        time.sleep(0.7)
        q2 = input("mit teszel?\n    nem csinálsz semmit(1)\n    Rázárod az ajtót(2)\n>>>")
        if q2 == "1":
            time.sleep(0.7)
            print("Erika kihozza a röpiket és megírod...")
            time.sleep(0.7)
            print("A röpdolgozat egyes lett")
            ertekeles.append("jegy: 1")
            q10 = input("Mit teszel?\n    Kimész az ajtón(1)\n    Maradsz és kivárod az óra végét(2)")
            if q10 == "1":
                print("kapsz egy igazolatlan órát")
                ertekeles.append("igazolatlan óra")
                time.sleep(0.7)
                print(f"Az eredményeid:\n    {ertekeles[0]}\n    {ertekeles[1]}, ")
            if q10 == "2":
                print("Kivártad az óra végét.")
                print(f"Az eredményeid:\n    {ertekeles[0]}")
                
        if q2 == "2":
            time.sleep(0.7)
            print("Erika a szertárban található sósavval kimarja a falat és beír egy szaktanárit.")
            ertekeles.append("Szaktanári")
            time.sleep(0.7)
            print("12:30 :: Ezzel sok idő eltelt szóval a röpi elmarad")
            time.sleep(0.7)
            print("Erika az írásvetítő alá beteszi a fóliát...")
            time.sleep(0.7)
            q7 = input("mit teszel?:\n    Alszol(1)\n    írod a szöveget(2)\n>>>")
            if q7 == "1":
                print("az óra eltelt kibírtad...")
                time.sleep(0.7)
                print(f"Az eredményeid:\n    {ertekeles[0]}\n    {ertekeles[1]}, ")
            if q7 == "2":
                print("Leírtad a szöveget és eltelt az óra")
                print(f"Az eredményeid:\n    {ertekeles[0]}\n    {ertekeles[1]}, ")



    if q1 == "2":
        time.sleep(0.7)
        print("Erika beír egy egyest.")
        ertekeles.append('Jegy: 1')
        time.sleep(1)
        print("Erika bemegy a szertárba...")
        time.sleep(0.7)
        q3 = input("mit teszel?\n    nem csinálsz semmit(1)\n    Rázárod az ajtót(2)\n>>>")
        if q3 == "1":
            time.sleep(0.7)
            print("12:30 :: sok idő eltelt szóval a röpi elmarad")
            time.sleep(0.7)
            print("Erika az írásvetítő alá beteszi a fóliát...")
            time.sleep(0.7)
            q4 = input("mit teszel?:\n    Alszol(1), írod a szöveget(2)")
            if q4 == "1":
                print("az óra eltelt kibírtad...")
                time.sleep(0.7)
                print(f"Az eredményeid: {ertekeles[0]}")
            if q4 == "2":
                print("Leírtad a szöveget és eltelt az óra")
                print(f"Az eredményeid:\n    {ertekeles[0]}\n    {ertekeles[1]}, ")

        if q3 == "2":
            time.sleep(0.7)
            print("Erika a szertárban található sósavval kimarja a falat és beír egy szaktanárit.")
            ertekeles.append("Szaktanári")
            time.sleep(0.7)
            print("12:30 :: Ezzel sok idő eltelt szóval a röpi elmarad")
            time.sleep(0.7)
            print("Erika az írásvetítő alá beteszi a fóliát...")
            time.sleep(0.7)
            q5 = input("mit teszel?:\n    Alszol(1)\n    írod a szöveget(2)\n>>>")
            if q5 == "1":
                print("az óra eltelt kibírtad...")
                time.sleep(0.7)
                print(f"Az eredményeid:\n    {ertekeles[0]}\n    {ertekeles[1]}")


if __name__ == "__main__":
    main()