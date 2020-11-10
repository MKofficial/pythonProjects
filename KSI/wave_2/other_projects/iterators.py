class Klazz:
    def __init__(self, iterable, start=0):
        self.i = start
        self.it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        result = self.i, next(self.it)
        self.i += 1
        return result


a = Klazz([1, 2, 3])
print(dict(a), list(a), sum(a))