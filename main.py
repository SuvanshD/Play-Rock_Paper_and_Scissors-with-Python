import random
choices = ['Rock','Paper','Scissor']
player = False
CPU_score = 0
Player_score = 0

while True:
    computer = random.choice(choices)
    
    player = input("Rock, Paper or  Scissors?").capitalize()
    print("")
    
    if  player == computer:
        print("It's a tie")
    
    elif  player == 'Rock':
        if  computer == 'Paper':
            print("You lose!", computer, "covers", player)
            CPU_score += 1
        else :
           print("You win!", player, "smashes", computer)
           Player_score +=1 
    elif  player == 'Scissor':
        if  computer == 'Rock':
            print("You lose!", computer, "smashes", player)
            CPU_score += 1
        else :
           print("You win!", player, "cut", computer)
           Player_score +=1 
    elif  player == 'Paper':
        if  computer == 'Scissor':
            print("You lose!", computer, "cut", player)
            CPU_score += 1
        else :
           print("You win!", player, "covers", computer)
           Player_score +=1 
           
    elif player == 'End':
        print("Final scores:")
        print("CPU : {}".format(CPU_score))
        print("Player : {}".format(Player_score))
        break