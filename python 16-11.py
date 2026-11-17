min=0
max=100

for i in range(max):
    a=(min+max)//2
        b=input(f"is your number{a}? (YES/NO,greater/less)")
        if (b=='greater'):
            min=a
            a=(min+max)//2
        elif (b=='lesser'):
            max=a
            a=(min+max)//2
        else:
            print('yes,your number is',a)