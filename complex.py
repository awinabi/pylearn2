class Complex:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, c2):
        return Complex(self.x + c2.x, self.y + c2.y)

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)


c1 = Complex(1, 2)
c2 = Complex(4, -1)
c3 = Complex()

print(c1)
print(c1 + c2)
print(c3)
