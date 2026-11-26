
import random

def nyeroszamok():
    szamok = random.sample(range(1, 46), 6)

    # for i in range(6):
    #     szamok.append(random.randint(1, 45))
    return szamok


def main():
    szamok = nyeroszamok()
    osszeg = sum(szamok)
    szorzat = 1
    for szam in szamok:
        szorzat *= szam
    print(f"Nyerőszámok: {szamok}")
    print(f"Összeg: {osszeg}")
    print(f"Szorzat: {szorzat}")

if __name__ == "__main__":
    main()