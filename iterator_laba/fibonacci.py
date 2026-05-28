class FibonacchiLst:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

        # заранее создаём множество чисел Фибоначчи до max элемента списка
        self.fib_set = self._build_fib_set(max(instance) if instance else 0)

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.instance):
            value = self.instance[self.idx]
            self.idx += 1

            if value in self.fib_set:
                return value

        raise StopIteration

    def _build_fib_set(self, limit):
        fib = set()
        a, b = 0, 1

        while a <= limit:
            fib.add(a)
            a, b = b, a + b

        return fib