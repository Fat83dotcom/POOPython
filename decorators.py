import time
from functools import lru_cache


def register(func):
    def registered(*args):
        with open('registerLog.txt', 'a+', encoding='utf-8') as log:
            ini = time.time()
            result = func(*args)
            end = time.time()
            totalTime = end - ini
            date = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
            log.write(f'{date} -> time relapsed: {totalTime}\n')
        return result
    return registered


@register
def f1(text):
    print(f'running f1({text})')
    time.sleep(2)


@lru_cache()
@register
def fibo(n) -> int:
    if n < 2:
        return n
    return fibo(n-2) + fibo(n - 1)


if __name__ == '__main__':
    f1('Mantegoso')
    print(fibo(500))
