def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(m):
    return lambda x: x % m > 0


def primes():
    yield 2
    it = _odd_iter()   # 初始化序列
    while True:
        n = next(it)   # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(m), it)  # 构造新序列


for n in primes():
    if n < 100:
        print(n)
    else:
        break

