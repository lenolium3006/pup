import functools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res

g = fib_elem_gen()

while True:
    el = next(g)
    print(el)
    if el > 10:
        break
        
 
       

def my_genn():
    """Сопрограмма"""

    while True:
        number_of_fib_elem = yield

        # базовые случаи
        if number_of_fib_elem is None or number_of_fib_elem <= 0:
            yield []
            continue

        # генерация Фибоначчи
        l = []
        a, b = 0, 1

        for _ in range(number_of_fib_elem):
            l.append(a)
            a, b = b, a + b

        yield l

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


my_genn = fib_coroutine(my_genn)
gen = my_genn()
print(gen.send(5))