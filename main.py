from utils import secti, obsah_trojuhelniku


def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    obsah_trojuhelniku(1,x,y)
    print(f"Obsah trojuhelniku {x} a {y} je: {vysledek}")

if __name__ == '__main__':
    main()
