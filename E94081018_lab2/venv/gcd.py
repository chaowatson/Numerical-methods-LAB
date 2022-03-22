# gcd function
def gcd(m: int, n: int) -> int:
    """ function of finding a greatest common divisor """
    # m>n
    if n * m == 0:
        print("---------------------------------------\n"
              "Please enter a number greater than zero\n"
              "---------------------------------------")
        first = input("Enter first positive integer (m):")
        second = input("Enter second positive integer (n):")
        m = int(first)
        n = int(second)
        gcd(m, n)
    elif m >= n:
        while m % n != 0:
            temp = n
            n = m % n
            m = temp
        print(f"Greatest common divisor: {n}", end='')
        return n
    # n>m
    elif n >= m:
        while n % m != 0:
            temp = m
            m = n % m
            n = temp
        print(f"Greatest common divisor: {m}", end='')
        return m

gcd(0,5)