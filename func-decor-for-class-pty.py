"""
    Пример функции-декоратора для создания атрибута свойство для класса
"""
def decor(name):
    def wrapper(Class):
        def wrapper2():
            privateName = '__' + name
            def getter(self):
                return getattr(self, privateName)
            def setter(self):
                setattr(self, privateName)
            setattr(Class, name, property(getter, setter))
            return Class
        return wrapper2
    return wrapper

@decor('x')
class MyClass:
    pass

o = MyClass()
o.x = 14
print(o.x)
