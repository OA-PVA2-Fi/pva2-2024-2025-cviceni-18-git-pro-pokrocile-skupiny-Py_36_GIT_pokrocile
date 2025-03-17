from utils import secti,deleni

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Výsledek dělení {x} a {y} je: {deleni(x, y)}")

if __name__ == '__main__':
    main()