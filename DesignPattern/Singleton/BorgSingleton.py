class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


class Singleton(Borg):
    def __init__(self, arg):
        # Borg.__init__(self)
        super(Singleton, self).__init__()
        self.val = arg

    def __str__(self):
        return self.val

    # def __getattr__(self, name):
    #     return getattr(self, name)
    #
    # def __setattr__(self, name):
    #     return setattr(self, name)


x = Singleton("sausage")
print(x)

y = Singleton("eggs")
print(y)

z = Singleton("spam")
print(z)

print(y)
print(x)

z.dynamic_add_string = "dynamic add string 1"
print(x.dynamic_add_string)

z.dynamic_add_string = "dynamic add string 2"
print(y.dynamic_add_string)