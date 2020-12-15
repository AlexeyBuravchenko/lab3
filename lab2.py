class Weight:
    def __init__(self, m):
        self.m = m

    def __add__(self, n):
        res = self.m + n
        return res

    def __sub__(self, n):
        if n > self.m:
            raise ValueError
        res = self.m - n
        return res

    def __mul__(self, n):
        res = self.m * n
        return res


m = Weight(578.32)
print(m.__add__(24))
print(m.__sub__(78.32))
print(m.__mul__(45))