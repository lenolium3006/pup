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
        print(number_of_fib_elem)
        number_of_fib_elem = yield
        a = 0
        b = 1
        l = []
        for i in range(number_of_fib_elem):
            l.append(a)
            a, b = b, a + b
        l = [str(number_of_fib_elem)+":", 0, 1, 1] # example data
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