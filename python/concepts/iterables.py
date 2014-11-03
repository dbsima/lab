class Fibonacci(object):
    """
    __iter__(self) is implicitly called by iter() and is responsive for
    retuning an iterator that Python can use to retrieve items from the object

    The __iter__(self) method implemented bellow is defined as a generator
    function
    """
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        a, b = 0, 1
        for x in range(self.count):
            if x < 2:
                yield x
            else:
                c = a + b
                yield c
                a, b = b, c

for x in Fibonacci(5):
    print x


class FibonacciIterator(object):
    def __init__(self, count):
        self.a = 0
        self.b = 1
        self.count = count
        self.current = 0

    def __next__(self):
        self.current += 1
        if self.current > self.count:
            raise StopIteration
        if self.current < 3:
            return self.current - 1
        c = self.a + self.b
        self.a = self.b
        self.b = c
        return c

    # Support for both Python 2 and 3
    next = __next__

    def __iter__(self):
        # Since it's already an iterator, this can return itself
        return self


class FibonacciV2(object):
    """

    """
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return FibonacciIterator(self.count)

for x in FibonacciV2(5):
    print x
