import math
def secti(a, b):
    """
    Vrátí součet dvou čísel.

    :param a: první číslo
    :param b: druhé číslo
    :return: součet a a b
    """
    return a + b

# Příklad další funkce, kterou můžete procvičit při vytváření nové větve
def odecti(a, b):
    """
    Vrátí rozdíl dvou čísel.

    :param a: první číslo
    :param b: druhé číslo
    :return: rozdíl a a b
    """
    return a - b

def deleni(a,b):
    return a / b

def obsah_trojuhelniku(volba, a, b, c=0, uhel=0):
    if volba == 1:
        return 0.5 * a * b
    elif volba == 2:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    elif volba == 3:
        return 0.5 * a * b * math.sin(math.radians(uhel))

