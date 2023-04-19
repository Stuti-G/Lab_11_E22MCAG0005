from Duck import Duck
from FlyWithWings import FlyWithWings
from MuteQuack import MuteQuack


class RedHeadDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a real Red Headed duck")
