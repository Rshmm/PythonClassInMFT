import random

class Human:

    def __init__(self, name):
        self.name = name




humans = [
    Human("reza"),
    Human("ali"),
    Human("arsham"),
    Human("arash"),
    Human("armita")
]


boss = random.choice(humans)
boss.is_boss = True


for human in humans:
    if hasattr(human,"is_boss"):
        print(f"{human.name} is boss", human.is_boss)
    else:
        print(f"{human.name} is not boss")