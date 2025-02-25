class roots:
    def __init__(self, value, tol = 0.0001):
        self.value = value
        self.tol = tol

    def findroot(self):
        current = self.value // len(str(self.value))
        previous = 0
        while abs(current - previous) > self.tol:
            next = current - self.ratio(current)
            previous = current
            current = next
        return next#previous

    def function(self, x):
        return x ** 2 - self.value

    def derivative(self, x):
        return 2 * x ** 1

    def ratio(self, x):
        return self.function(x) / self.derivative(x)

test = roots(4000, 0.001)
root = test.findroot()
print(root)
print(root ** 2)