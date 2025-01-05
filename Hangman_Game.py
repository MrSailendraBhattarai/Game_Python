import random

word=['apple','ball','cat','dog']
choosen_word=random.choice(word)
print(choosen_word)
display=[]

for i in range (len(choosen_word)):
    display +='_'
print(display)
print("You have 8 Lives")
n=8
game=True
while game:
    for i in range(n):
        guess_letter=input("Enter a letter>>> ").lower()
        if guess_letter in choosen_word:
            for position in range (len(choosen_word)):
                letter=choosen_word[position]
                if letter==guess_letter:
                    display[position]=guess_letter
            print(display)

            if '_' not in display:
                game=False
                print("You Win.")
        elif guess_letter not in choosen_word:
            n-=1
            print("Wrong Letter!!")
            print(f"You have {n} lives left..")
            if n==0:
                game=False
                print("You loose!!")