from MallardDuck import MallardDuck
from RubberDuck import RubberDuck
from RedHeadDuck import RedHeadDuck
from DecoyDuck import DecoyDuck

class Main:
    @staticmethod
    def main():
        print("Select a duck to display its attributes:")
        print("a. Mallard Duck")
        print("b. Rubber Duck")
        print("c. Red Head Duck")
        print("d. Decoy Duck")
        choice = input("Enter the choice of your Duck : ")

        if choice == "a":
            duck = MallardDuck()
        elif choice == "b":
            duck = RubberDuck()
        elif choice == "c":
            duck = RedHeadDuck()
        elif choice == "d":
            duck = DecoyDuck()
        else:
            print("Incorrect Choice")
            return

        duck.display()
        duck.swim()
        duck.perform_quack_behavior()
        duck.perform_fly_behavior()

if __name__ == '__main__':
    Main.main()
