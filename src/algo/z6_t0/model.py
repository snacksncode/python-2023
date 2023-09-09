from dataclasses import dataclass


@dataclass
class Fraction:
    # ułamek = numer / denom
    numer: int
    denom: int

    def value(self):
        return self.numer / self.denom

"""
a/b + c/d = (a*d + c * b) / (b * d)

n1/d1 + n2/d2 = (n1*d2 + n2*d1) / (d1 * d2)

"""

if __name__ == '__main__':
    f = Fraction(1, 2)
    assert f.value() == 0.5
