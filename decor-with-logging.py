import sys

enable_tracing = True

if enable_tracing:
    debug_log = open('debug_log.txt', 'a', encoding='utf-8')

def logging(func):
    if enable_tracing:
        def wrapper(*args):
            debug_log.write('Вызов %s: %s\n' % (func.__name__, args))
            r = func(*args)
            debug_log.write('%s вернула %s\n' % (func.__name__, r))
            return r
        return wrapper
    else:
        return func

@logging
def square(x):
    return x*x

for i in range(10):
    print(square(i))

debug_log.close()
