from QuackBehavior import QuackBehavior


class MuteQuack(QuackBehavior):
    def quack(self):
        print("I can not speak")
