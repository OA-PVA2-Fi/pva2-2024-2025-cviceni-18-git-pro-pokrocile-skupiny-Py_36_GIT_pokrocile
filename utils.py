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

def obvod_ctverce(strana):
    return 4 * strana

strana = int(input("Zadejte délku strany čtverce: "))

obvod = obvod_ctverce(strana)

print(f"Obvod čtverce o straně {strana} je {obvod}.")

