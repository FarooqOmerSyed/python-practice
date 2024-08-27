import pytest
from fib_gen import fibonacci_generator
@pytest.mark.xfail
def test_fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen), end=" ")