# gcd function
def gcd(m: int, n: int) -> int:
    """ function of finding a greatest common divisor """
    # default of recursion
    if m == 0:
        return n
    elif n == 0:
        return m
    # m>n
    elif m >= n:
        return gcd(n, m % n)
    # n>m
    elif n >= m:
        return gcd(m, n % m)
