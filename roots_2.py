def root(x, n = 2, tolerance = 1e-8):
    def num(a):
        return (a ** n) - x
    def den(b):
        return n * (b ** (n - 1))
    if x < 0:
        return 'Unable to find root with given parameters'
    # elif n < 1:
    #     return 'Unable to find root with given parameters'
    # elif not isinstance(n, int):
    #     return 'Unable to find root with given parameters'
    else:
        xold = x + 1
        xnew = x // len(str(x))
        while abs(xnew - xold) > tolerance:
            xold = xnew

            xnew = xnew - (num(xnew) / den(xnew))
        # return xnew
    print(f'{x}^{1/n} is {xnew}')


print(root(1001, 1.5))