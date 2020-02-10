class OnlyOne:
    class __OnlyOne:
        def __init__(self, args):
            self.val = args
            self.index = 0

        def __str__(self):
            return repr(self) + self.val

        def get_next_index(self):
            self.index = self.index + 1

        def print_index(self):
            return print(str(self) + " " + str(self.index))

    instance = None

    def __init__(self, args):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(args)
        else:
            OnlyOne.instance.val = args

    def __getattr__(self, name):
        return getattr(self.instance, name)


x = OnlyOne("sausage")
x.get_next_index()
x.print_index()

y = OnlyOne("eggs")
y.get_next_index()
y.print_index()

z = OnlyOne("spam")
z.get_next_index()
z.print_index()

y.get_next_index()
y.print_index()

x.get_next_index()
x.print_index()






