import random

def start_game():
    print("--- Welcome to the Advanced Coin Guessing Game! ---")
    user_name = input("Enter your name to start: ")
    score = 0
    total_rounds = 3

    print(f"\nHello {user_name}! We will play {total_rounds} rounds.")

    for round_num in range(1, total_rounds + 1):
        print(f"\n--- Round {round_num} ---")
        print("Choose a method to toss the coin:")
        print("1. Using random.random()")
        print("2. Using random.randint()")
        
        # حلقة للتأكد من إدخال رقم صحيح (1 أو 2) بدون أن ينهار البرنامج
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice in ["1", "2"]:
                break
            print("Invalid input! Please enter 1 or 2 only.")

        # تحديد نتيجة الكمبيوتر
        if choice == "1":
            computer_result = "Heads" if random.random() >= 0.5 else "Tails"
        else:
            computer_result = "Heads" if random.randint(0, 1) == 0 else "Tails"

        # أخذ تخمين المستخدم
        user_guess = input("Enter your Guess (Heads or Tails): ").strip().capitalize()

        # مقارنة النتيجة
        if user_guess == computer_result:
            print(f"✅ Correct! The result was {computer_result}.")
            score += 1
        else:
            print(f"❌ Wrong! The result was {computer_result}.")

    # النتيجة النهائية
    print("\n" + "="*30)
    print(f"Game Over, {user_name}!")
    print(f"Your final score: {score} out of {total_rounds}")
    print("="*30)

# تشغيل اللعبة
start_game()


