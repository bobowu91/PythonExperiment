import sys
print(sys.executable)


class dish:

    def __init__(self, comp):
        self.comp = comp

    def shout(self):
        print(self.comp.veg)
        print("I can use comp's method say")
        self.comp.say()


class comp:

    def __init__(self, veg):
        self.veg = veg

    def say(self):
        print("This is {}".format(self.veg))


comp1 = comp("wululu")
comp1.say()

dish1 = dish(comp1)
dish1.shout()

#dish2 = dish()
