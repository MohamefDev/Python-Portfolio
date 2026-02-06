import os

while True:
    guessed = int(input("Guess the number between 1 and 10: "))
    
    if guessed != 5:
        print("wrong guess. try again")
        input("press anykey to continue...")
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    else:
        print("congratulation! you guessed the correct number.")
        break
