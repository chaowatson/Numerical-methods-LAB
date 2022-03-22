def factorial(a):  # using recursive func. to execute factorial calculation
    if a == 0:
        return 1
    if a > 0:
        return a*factorial(a-1)


def cos_approx(angle):  # calculate and print the cos of the input
    approx = 0
    N = 0
    while N <= 24:
        approx = approx + ((-1) ** (N/2)) * (angle ** N) / factorial(N)  # the function
        N += 2
    print(f"cos({angle}) approximation is {approx}")


cos_approx(2.3)