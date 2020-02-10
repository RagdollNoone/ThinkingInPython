class OnlyOne(object):
    class __OnlyOne:
        def __init__(self):
            self.val = None
            self.index = 0

        def __str__(self):
            return "self " + self.val

        def get_next_index(self):
            self.index = self.index + 1

        def print_index(self):
            return print(str(self) + " " + str(self.index))

    instance = None

    def __new__(cls):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne()

        return OnlyOne.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self, name)


x = OnlyOne()
x.val = "sausage"
x.get_next_index()
x.print_index()

y = OnlyOne()
y.val = "eggs"
y.get_next_index()
y.print_index()

z = OnlyOne()
z.val = "spam"
z.get_next_index()
z.print_index()

y.get_next_index()
y.print_index()

x.get_next_index()
x.print_index()

x.dynamic_add_string = "this is dynamic add string"
print(z.dynamic_add_string)

