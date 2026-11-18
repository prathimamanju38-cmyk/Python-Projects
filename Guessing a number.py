min=0
max=100
guess=(max+1)//2
print("Guess a number between 1 to 100")
for i in range(max):
        b=input(f"is your number {guess} (YES/NO,greater/less)")
        if(b == 'greater'):
            min=guess
            guess=(min+max)//2
            print(guess)
        elif(b == 'lesser'):
            max=guess
            guess=(max+min)//2
        elif(b == 'yes'):
            print(f"i guessed the number in {guess} in {i} number of steps")
            break;
        else:
            print("Enter the vaild response")
