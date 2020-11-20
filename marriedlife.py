from numpy.polynomial import polynomial as P

posPNXDict = {}
negPNXDict = {}


def posPNX(n):
    if n == 1:
        return (1)
    if n < 1:
        return
    if n in posPNXDict:
        return posPNXDict[n]
    first = P.polymul((1, 2*n - 2), posPNX(n-1))
    second = P.polymul((0, 4), (1, -1))
    deriv = P.polyder(posPNX(n-1))
    second = P.polymul(second, deriv)
    third = P.polymul((0, 1), (negPNX(n-1)))
    ret = P.polyadd(first, second)
    ret = P.polyadd(ret, third)
    posPNXDict[n] = ret
    return ret


def negPNX(n):
    if n == 1:
        return (1)
    if n < 1:
        return
    if n in negPNXDict:
        return negPNXDict[n]
    first = P.polymul((3, 2*n - 4), negPNX(n-1))
    second = P.polymul((0, 4), (1, -1))
    deriv = P.polyder(negPNX(n-1))
    second = P.polymul(second, deriv)
    third = posPNX(n-1)
    ret = P.polyadd(first, second)
    ret = P.polyadd(ret, third)
    negPNXDict[n] = ret
    return ret


for i in range(20):
    print(posPNX(20-i))
    print(negPNX(20-i))
    print(P.polyadd(posPNX(20-i), negPNX(20-i)))
