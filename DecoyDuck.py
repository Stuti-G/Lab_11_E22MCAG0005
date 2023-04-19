from Duck import Duck
from FlyNoWay import FlyNoWay
from MuteQuack import MuteQuack


class DecoyDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a duck Decoy")
