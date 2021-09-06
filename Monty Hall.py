import random
doors=[0]*3
goatdoors=[0]*2
swap=0
dontswap=0
x=random.randint(0, 2)
doors[x]="BMW"
for i in range(0,3):
    if(i==x):
        continue
    else:
        doors[i]="Goat"
        goatdoors.append(i)
choice=int(input("Enter Your Choice"))
door_open=random.choice(goatdoors)
while(door_open==choice):
    door_open=random.choice(goatdoors)
ch=input("Swap?(Y/N)")
if(ch=="y"):
    if(doors[choice]!="goat"):
        print("you win")
        swap+=1
    else:
        print("you lose")
else:
    if(doors[choice]!="goat"):
        print("you win")
        dontswap+=1
    else:
        print("you lose")