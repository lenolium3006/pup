from gen_fib import my_genn

def test_fib_1():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"

    
def test_fib_2():
    gen = my_genn()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов ряда"

def test_fib_zero():
    gen = my_genn()
    assert gen.send(0) == []

def test_fib_one():
    gen = my_genn()
    assert gen.send(1) == [0]
    
def test_fib_two():
    gen = my_genn()
    assert gen.send(2) == [0, 1]


def test_fib_multiple_calls():
    gen = my_genn()
    assert gen.send(3) == [0, 1, 1]
    assert gen.send(4) == [0, 1, 1, 2],"Проверка, что корутина работает несколько раз" 