def solution(n, m):
    temp = n
    big = max(n,m)
    small = min(temp,m)
    while (big % small != 0):
        temp = big%small
        big = small
        small = temp
    gcd = small
    lcm = n * m // gcd
    return [gcd, lcm]