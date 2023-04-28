import random
def RulePlay(name):
    print(f'''\n\n\nHey {name} welcome to the game of guessing a  number.
Lemme me quickly explain how this game works.
So basically at the very beginning you will get a demo
play for guessing the number to make you  understand 
how this works.
Then the original game begins.You will encounter 3 levels
Easy,Medium and Hard''')
def demoplay():
    if input('\n\nPress Y whenever you are ready\n').upper()=='Y':
        print('\n\nThe game begins\n\n')
        tries =0
        computer_choice = random.randint(0,25)
        while(True):
            t = int(input('Enter Your Guess:-\n'))
            tries+=1
            if t==computer_choice:
             print(f'\nHooray..!!\nYou have won the game\n')
             print('\nNow we can move on to the levels')
             break
            else:
                    if t<computer_choice:
                        print('\n\nOops..!! Wrong Guess\nYou Should have tried something greater')
                    else:
                        print('\n\nOops..!! Wrong Guess\nYou Should have tried something smaller')
def levelPlay(n):
    s=0
    computer_choice =0
    if n==1:
       s=10 
       computer_choice = random.randint(1,50)
       print('\n\nThis is the level 1\nTry your best to wipe the floor with it.\nLets Head on to blast it\n\n')
    elif n==2:
       s=10
       computer_choice = random.randint(1, 100)
       print('\n\nThis is the level 2\nTry your best to wipe the floor with it.\nLets Head on to blast it\n\n')
    else:
        computer_choice= random.randint(1,50)
        s = 5
        print('\n\nThis is the level 3\nTry your best to wipe the floor with it.\nLets Head on to blast it\n\n')
    guessed = False
    while not guessed and s>0:
        t = int(input('Enter Your Guess:-\n'))
        if t==computer_choice:
            guessed = True
        else:
            s-=1
            if s==0:
                if t<computer_choice:
                    print('\n\nOops..!! Wrong Guess\nYou Should have tried something greater')
                else:
                    print('\n\nOops..!! Wrong Guess\nYou Should have tried something smaller')
                print(f'The number is {computer_choice}')
            else:
                if t<computer_choice:
                    print('\n\nOops..!! Wrong Guess\nYou Should try something greater')
                else:
                    print('\n\nOops..!! Wrong Guess\nYou Should try something smaller')
                print(f'Remaining chances---->  {s}')
    if guessed==True:
        if n==3:
            print('\n\nHooray you Have won the game😎😎😎😎\nIf it was possible i could have sent you an iphone\n')
        else:
            print(f'Hooray you have cleared level {n}\nLets move on to the next level')
            levelPlay((n+1))
               
    else:
        print(f'So Sorry!!! You Lost on level {n} 😵‍💫😵‍💫😵‍💫😵‍💫😵‍💫')
                
                
                
                  
name = input('Enter Your Name to begin\n')
RulePlay(name)
demoplay()
print('Press Y to move on to the stages\n')
if input().upper()=='Y':
     levelPlay(1)