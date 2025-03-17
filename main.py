from utils import secti
from utils import umocneni_cisel

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    vysledek_umocneni = umocneni_cisel(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Výsledek umocnění čísla {x} číslem {y} je: {vysledek_umocneni}")

if __name__ == '__main__':
    main()