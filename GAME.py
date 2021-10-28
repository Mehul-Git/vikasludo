import random  

def gamewin(computer , you):
    if computer == you:
        return None
    elif computer=="rock":
        if you=="paper":
            return True
        elif you=="scissor":
            return False
    elif computer=="scissor":
        if you=="rock":
            return True
        elif you=="paper":
            return False
    elif computer=="paper":
        if you=="scissor":
             return True
        elif you=="rock":
            return False

print("computer turn: rock, paper , scissor?")
randno = random.randint(1,3) 
if randno == 1:
    computer = "rock"
elif randno == 2:
    computer ="paper"
elif randno == 3:
    computer ="scissor"
you = input("enter yourn turn: rock, paper, scissor\n")
a = gamewin(computer, you)
print(f"computer choose this:{computer}")
print(f"you choose:{you}")
if (a == None):
    print("tie")
elif a:
    print("you win")
else:
    print("you lose")
