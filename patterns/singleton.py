
class Singleton:

    class __Singleton:
        def __init__(self, *args, **kwargs):
            self.value = args[0] or "kid"

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__Singleton(*args, **kwargs)
        return cls.instance

    def __getattr__(self, key):
        return getattr(self.instance, key)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)


one = Singleton("adult")
two = Singleton()
three = Singleton()

print(f"""Instances:
        one={one}
        two{two}
        three={three}""")
print(f"""Values:
        one.value={one.value}
        two.value={two.value}
        three.value={three.value}""")

print("Change three.value to 'kid'")
three.value = "kid"
print(f"""Values:
        one.value={one.value}
        two.value={two.value}
        three.value={three.value}""")
