class dish:

    def __init__(self, *comp):
        self.comp = comp

    def shout(self):
        print(self.comp.veg)
        print("I can use comp's method say")
        self.comp.say()

    def recipe(self):
        print("vice versa")


class comp:

    def __init__(self, veg):
        self.veg = veg

    def say(self):
        print("This is {}".format(self.veg))


comp1 = comp("tomato")
comp1.say()

comp2 = comp("spice")

comp1.dishrecipe = dish(comp2)
comp1.dishrecipe.recipe()

# dish1 = dish(comp1)
# dish1.shout()

dish2 = dish()
dish2.comp = comp1
dish2.shout()
