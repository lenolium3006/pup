
class FibonacchiLst:

    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

        # множество чисел Фибоначчи
        self.fib_numbers = {0, 1, 2, 3, 5, 8, 13, 21}


    def __iter__(self):
        return self


    def __next__(self):

        while True:

            if self.idx >= len(self.instance):
                raise StopIteration

            value = self.instance[self.idx]
            self.idx += 1

            if value in self.fib_numbers:
                return value