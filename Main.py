from MallardDuck import MallardDuck
from RubberDuck import RubberDuck
from RedHeadDuck import RedHeadDuck
from DecoyDuck import DecoyDuck

class Main:
    @staticmethod
    def main():
        print("Select a duck to display its attributes:")
        print("1. Mallard Duck")
        print("2. Rubber Duck")
        print("3. Red Head Duck")
        print("4. Decoy Duck")
        choice = input("Enter your choice: ")

        if choice == "1":
            duck = MallardDuck()
        elif choice == "2":
            duck = RubberDuck()
        elif choice == "3":
            duck = RedHeadDuck()
        elif choice == "4":
            duck = DecoyDuck()
        else:
            print("Invalid choice")
            return

        duck.display()
        duck.swim()
        duck.perform_quack_behavior()
        duck.perform_fly_behavior()

if __name__ == '__main__':
    Main.main()
