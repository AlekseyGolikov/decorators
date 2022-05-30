# Программа выполняет декорируемую функция count_iter раз,
# а затем выводит среднее время выполнения

import requests
import time

def benchmark(count_iter):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(count_iter):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total += (end - start)
                print("Вызов %d" % i)
            print("[*] Среднее значение выполнения {} секунд".format(total/count_iter))
            return return_value
        return wrapper
    return actual_decorator

@benchmark(count_iter=3)
def fetch_webpage(url):
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage('https://google.com')
print(webpage)
