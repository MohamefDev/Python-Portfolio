import os
import random

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# توليد الرقم المطلوب
target_number = random.randint(1, 10)

while True:
    clear_screen()
    
    # طلب التخمين من المستخدم
    try:
        user_input = input("Enter a number from 1 to 10: ")
        guessed = int(user_input)
    except ValueError:
        print("Please enter a valid number!")
        input("press any key to continue...")
        continue

    # التحقق من النتيجة
    if target_number == guessed:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")
        input("press any key to continue...")
