import random
words=["moh","ikram","chiama"]
random_word=random.choice(words)
display=["_"]*len(random_word)
print(' '.join(display))
lives=6
while "_" in display and lives>0:
    guessed =input("please guess a letter: ").lower()
    if guessed not in random_word:
        lives-=1
    
    
    
    for position in range(len(random_word)):
        if random_word[position]==guessed:
            display[position] =guessed
    print(display)
    print(f"you have {lives} more tries")



if lives==0:
    print("you lost!")
    print("""
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
         """)
else:
    print("""
***********
_____.___.                      .__        
\__  |   | ____  __ __  __  _  _|__| ____  
 /   |   |/  _ \|  |  \ \ \/ \/ /  |/    \ 
 \____   (  <_> )  |  /  \     /|  |   |  \
 / ______|\____/|____/    \/\_/ |__|___|  /
 \/                                     \/ 
********** 
         """)

                                                         