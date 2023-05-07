class Player:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("my name is " + self.name, "color" + self.color, self.weight)


r1 = Player("bryan", "blanco", 70)
r2 = Player("migue", "negro", 60)


class Person:
    def __init__(self, name, personality, esta):
        self.name = name
        self.personality = personality
        self.esta = esta

    def itis_angry(self):
        self.is_angry = True

    def itis_not_angry(self):
        self.is_angry = False
        print(self.name)


p1 = Person("oda", "calm", False)
p2 = Person("mayi", "happy", True)

# p1 owns r2
p1.Player_mom = r2
p2.Player_mom = r1

p1.Player_mom.introduce_self()
p1.itis_not_angry()
