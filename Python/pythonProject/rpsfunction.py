def rps():
    while True:
        option = input("Play Rock/paper/scissors ,enter yes/no")
        if option == 'yes':
            x = input(" x-select rock/paper/scissors")
            y = input(" y-select rock/paper/scissors")
            if x == y:
                print("its a tie")
            elif x == 'rock' and y == 'paper':
                print("y wins")

            elif x == 'rock' and y == 'scissor':
                print("x wins")

            elif x == 'paper' and y == 'scissor':
                print("y wins")

        else:
            print("would you like to play again")
            break
rps();