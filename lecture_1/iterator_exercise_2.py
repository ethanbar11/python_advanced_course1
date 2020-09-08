class RangeI:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = start

    def __iter__(self):
        return RangeIterator(self)


class RangeIterator:
    def __init__(self, range_i):
        self.start = range_i.start
        self.end = range_i.end
        self.i = self.start

    def __next__(self):
        if self.start <= self.i < self.end:
            self.i += 1
            return self.i - 1
        else:
            raise StopIteration()
