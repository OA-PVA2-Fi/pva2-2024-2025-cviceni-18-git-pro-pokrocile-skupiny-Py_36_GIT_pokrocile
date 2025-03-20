from utils import secti, obvod_kruznice

def main():
    x = 5
    y = 10
    r = 5
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Výsledek obvodu kružnice s poloměrem {r} je: {obvod_kruznice(r)}")

if __name__ == '__main__':
    main()