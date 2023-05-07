class figter:
    def __init__(self, name, punch, speed):
        self.name = name
        self.punch = punch
        self.speed = speed

    def say_someting(self):
        print("my name is " + self.name)


p1 = figter("bryan", 80, 30)
p2 = figter("mige", 60, 100)

p1.say_someting()


class sword:
    def __init__(self, cut):
        self.cut = cut


s1 = sword(50)

s1.figter_w = p1

s1.figter_w.say_someting()
