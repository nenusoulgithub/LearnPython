# 单例
class Animal:
    __instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return Animal.__instance


dog = Animal("旺财")
print(id(dog))
dog = Animal("旺财")
print(id(dog))
dog = Animal("旺财")
print(id(dog))
dog = Animal("旺财")
print(id(dog))