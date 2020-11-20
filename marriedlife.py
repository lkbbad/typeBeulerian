from numpy.polynomial import polynomial as P


def posPNX(n):
    if n == 1:
        return (1)
    if n < 1:
        return
    first = P.polymul((1, 2*n - 2), posPNX(n-1))
    second = P.polymul((0, 4), (1, -1))
    deriv = P.polyder(posPNX(n-1))
    second = P.polymul(second, deriv)
    third = P.polymul((0, 1), (negPNX(n-1)))
    ret = P.polyadd(first, second)
    return P.polyadd(ret, third)


def negPNX(n):
    if n == 1:
        return (1)
    if n < 1:
        return
    first = P.polymul((3, 2*n - 4), negPNX(n-1))
    second = P.polymul((0, 4), (1, -1))
    deriv = P.polyder(negPNX(n-1))
    second = P.polymul(second, deriv)
    third = posPNX(n-1)
    ret = P.polyadd(first, second)
    return P.polyadd(ret, third)


for i in range(1, 5):
    print(posPNX(i))
    print(negPNX(i))
