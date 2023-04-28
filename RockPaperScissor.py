import random
def choice(n):
    return 'Rock' if n==1 else 'Scissor' if n==3 else 'Paper'
def gameplay(user):
    computer_choice = random.randint(1,3)
    user_choice=int(input('What would you like to choose.Select the corresponding number\n1.Rock\n2.Paper\n3.Scissor\n'))
    winner = user if ((user_choice==1 and computer_choice==3) or (user_choice==2 and computer_choice==1) or (user_choice==3 and computer_choice==2)) else 'computer'
    print('Your choice was \n',choice(user_choice))
    print('The computer''s choice was \n',choice(computer_choice))
    if user_choice==computer_choice:
        print('OH.. its a draw')
    else:
        print(f'The winner is......\n{winner}')
name = input('Enter your name\n')
gameplay(name)
while (input('Would You like to play again?\nY for yes\nN for no')).upper()=='Y':
    c = input('Would You like to play again with the same name of you want to change it?\nY for yes\nN for no')
    if c=='Y':
        name = input('Enter the name you want\n')
    gameplay(name)