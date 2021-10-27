while True:
    option = input("Play Rock/paper/scissors ,enter yes/no")
    if option == 'yes':
        x = input(" x-select rock/paper/scissors")
        y = input(" y-select rock/paper/scissors")
        if x == y:
            print("its a tie")
        elif x == 'rock':
            if y == 'paper':
                print("y wins")
            else:
                print("x wins")

        elif x == 'rock':
            if y == 'scissor':
                print("x wins")
            else:
                print("y wins")
        elif x == 'paper':
            if y == 'scissor':
                print("y wins")
            else:
                print("x wins")
    else:
        print("would you like to play again")
        break



