# Если нельзя изменять определение некоего класса,
# но хочется добавить новый атрибут, то можно применить
# следующий пример

def decorator(cls):
    class Wrapper(cls):
        def doubler(self, value):
            return value * 2
    return Wrapper

@ decorator
class MyActualClass:
    def __init__(self):
        print("in MyActualClass __init__()")
    def guad(self, value):
        return value * 4

obj = MyActualClass()
print(obj.guad(4))
print(obj.doubler(4))
