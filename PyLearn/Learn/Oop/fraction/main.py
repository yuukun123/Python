from fraction import Fraction

if __name__ == '__main__':
    f = Fraction()
    n = int(input("Nhap so luong phan so: "))
    fractions = f.inputListFraction(n)
    f.showFraction(fractions)
    for frac in fractions:
        frac.simplify()
    f.showFraction(fractions)
    print()
    f.reversedList(fractions)

    f.addFractions(fractions)
    f.subFractions(fractions)
    f.mulFractions(fractions)
    f.divFractions(fractions)

