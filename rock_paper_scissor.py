import random

user_wins=0
computer_wins=0
option=['rock','paper','scissor']
# option=['0','1','2']
while True:
    user_input=input('Type Rock/Paper/Scissor or Q to quit:').lower()
    if user_input=='q':
        break
    if user_input not in option:
        continue
    random_number = random.randint(0,2)
    # rock:0, paper:1, scissor:2
    computer_pick= option[random_number]
    print("computer picked",computer_pick+".")

    if user_input =='rock' and computer_pick=="scissor":
        print ('you win!')
        user_wins+=1
    elif user_input =='paper' and computer_pick=="rock":
        print ('you win!')
        user_wins+=1
    elif user_input =='scissor' and computer_pick=="paper":
        print ('you win!')
        user_wins+=1   
    elif user_input == computer_pick:
        print("You and the computer tied!")
        continue
    else:
        print("you lost!")
        computer_wins+=1
print('you won',user_wins,'times')
print('computer won',computer_wins,'times')
print("Good Bye!")