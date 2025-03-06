from utils import secti, nasob


def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")

if __name__ == '__main__':
    main()


def nasobeni():
    a = 3
    b = 5
    vysledek_nasob = nasob(a,b)
    print (f'Výsledek násobení {a} a {b} je: {vysledek_nasob}')

