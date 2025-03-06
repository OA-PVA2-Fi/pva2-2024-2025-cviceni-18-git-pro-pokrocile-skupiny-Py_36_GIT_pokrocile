from utils import secti, nasob

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")

def priklad_nasobeni():
    x = 5
    y = 5
    vysledek = nasob(x, y)
    print(f"Výsledek násobení {x} a {y} je: {vysledek}")

if __name__ == '__main__':
    main()

priklad_nasobeni()