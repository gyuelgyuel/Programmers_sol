import math
def solution(numer1, denom1, numer2, denom2):
    denom = lcm(denom1, denom2)
    numer = numer1*(denom//denom1) + numer2*(denom//denom2)
    gcd1 = math.gcd(denom, numer)
    return [numer//gcd1, denom//gcd1]

def lcm(n1, n2):
    temp = n1
    big = max(n1,n2)
    small = min(temp,n2)
    while (big%small!=0):
        big = big%small
        temp = big
        big = max(big,small)
        small = min(temp,small)
    gcd = small
    return n1 * n2 // gcd