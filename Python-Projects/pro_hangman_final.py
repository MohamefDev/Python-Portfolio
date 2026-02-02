import random

# قائمة الرسومات تمثل مراحل الخسارة (من 6 محاولات إلى 0)
STAGES = [
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / \\
       -
    """, # 0 محاولات (خسارة)
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |     / 
       -
    """, # محاولة واحدة
    """
       --------
       |      |
       |      O
       |     /|\\
       |      |
       |      
       -
    """, # محاولتان
    """
       --------
       |      |
       |      O
       |     /|
       |      |
       |     
       -
    """, # 3 محاولات
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |     
       -
    """, # 4 محاولات
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       -
    """, # 5 محاولات
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       -
    """  # 6 محاولات (بداية اللعبة)
]

words = ["python", "developer", "algeria", "github", "cipher"]
chosen_word = random.choice(words)
word_length = len(chosen_word)
display = ["_"] * word_length
lives = 6

print("Welcome to HANGMAN!")

while "_" in display and lives > 0:
    # طباعة الرسم بناءً على عدد المحاولات المتبقية
    print(STAGES[lives])
    print(f"Word: {' '.join(display)}")
    print(f"Lives remaining: {lives}")
    
    guess = input("Please guess a letter: ").lower()

    # إذا كرر اللاعب حرفاً تم تخمينه سابقاً
    if guess in display:
        print(f"You already guessed '{guess}', try another letter.")
        continue

    # التحقق من وجود الحرف في الكلمة
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Good job! Correct letter.")
    else:
        lives -= 1
        print(f"Wrong! The letter '{guess}' is not in the word.")

# نتيجة اللعبة النهائية
if "_" not in display:
    print(f"\nCongratulations! You won! 🏆 The word was: {chosen_word}")
else:
    print(STAGES[0])
    print(f"\nGAME OVER! 💀 The word was: {chosen_word}")

                                                         
