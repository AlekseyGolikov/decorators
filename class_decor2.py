"""
    Пример функции-декоратора, которая добавляет атрибут в декорируемый класс без применения наследования
"""
def is_in_range(minNum, maxNum):
    def is_in_range(value):
        """
            Функция-замыкание для проверки диапазона значения переменной value
        """
        if not isinstance(value, int):
            raise TypeError('Значение должно быть типа int')
        if value < minNum:
            raise ValueError('Значение должно быть меньше {}!'.format(minNum))
        elif value>maxNum:
            raise ValueError('Значение не должно превышать {}!'.format(maxNum))
    return is_in_range

def ensure(name, validator, doc=None):
    """
    Функция-декоратор позволяет добавить новое свойство в декорируемый класс
    :param name: имя для создаваемого свойства
    :param validator: функция проверки значения свойства
    :param doc: строка документирования
    :return: декорируемый класс
    """
    def wrapper(Class):
        privateName = '__'+name
        def getter(self):
            return getattr(self, privateName)
        def setter(self, value):
            validator(value)
            setattr(self, privateName, value)

        setattr(Class, name, property(getter, setter, doc=doc))
        return Class
    return wrapper

@ensure('x', is_in_range(0,10))
class Obj:
    pass

o = Obj()

o.x = 5
print(o.x)
o.x = 11
print(o.x)
