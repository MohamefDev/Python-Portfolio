import random

print("Welcome to the Coin Guessing Game!")

print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")

choice = input("Enter your choice (1 or 2): ")

# تحديد نتيجة الكمبيوتر بناءً على الطريقة المختارة
if choice == "1":
    random_number = random.random()
    if random_number >= 0.5:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
        
elif choice == "2":
    if random.randint(0, 1) == 0:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
else:
    print("Invalid choice. Please select either 1 or 2.")
    # إنهاء البرنامج في حال الاختيار الخاطئ لتجنب حدوث خطأ لاحقاً
    
user_choice = input("Enter your Guess (Heads or Tails)")
if user_choice.lower() == computer_result.lower():
    print("Congratulations! You won!")
else:
    print(f"Sorry, you lost! The result was {computer_result}.")

