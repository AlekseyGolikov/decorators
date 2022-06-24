"""
    Пример функции-декоратора для создания атрибута свойство для класса
"""
def decor(name):
    def wrapper(cls):
        def wrapper2():
            privateName = '__' + name
            def getter(self):
                return getattr(self, privateName)
            def setter(self):
                setattr(self, privateName)
            setattr(cls, name, property(getter, setter))
            return cls
        return wrapper2
    return wrapper

@decor('x')
class MyClass:
    pass

o = MyClass()
o.x = 12
print(o.x)
