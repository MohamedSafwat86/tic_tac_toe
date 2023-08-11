from functools import reduce
from random import randint

def Draw_Board(Board_List):
    print("-"*40)
    for j in range(3):
        print((("|"+" "*12)*3)+"|")
        print((("|"+" "*12)*3)+"|")
        for i in range(3):
            print((("|"+" "*5)+"{0}"+(" "*6)).format(Board_List[j][i] if type(Board_List[j][i])!=str else "\033[1m" + Board_List[j][i] + "\033[0m"),end="")
        else:
            print("|")
        print((("|"+" "*12)*3)+"|")
        print((("|"+" "*12)*3)+"|")
        print("-"*40)

def Take_Player_Movement(Board_List):
    while(True):
        try:
            move=int(input("Please,Enter Your Movement:"))
        except :
             print("Invalid input numbers only...")
        else:
            if move < 0 or move >9 :
                print("Out of Range Movement 'only(1~9)'")
                continue
            if type(Board_List[(move-1)//3][(move-1)%3])==str:
                print("The Square Is Already occuped")
                continue
            Board_List[(move-1)//3][(move-1)%3]=Player_Symbol
            Available_Movements.remove(move)
            Draw_Board(Board_List)
            break
        
        
def AI_Movement(Available_Movements):
    move=Available_Movements[randint(0,len(Available_Movements)-1)]
    Board_List[(move-1)//3][(move-1)%3]=AI_Symbol
    Available_Movements.remove(move)
    Draw_Board(Board_List)
    
    
def Check_Win(Board_List,Symbol):
    for i in range(0,3):
            if all([True if x==Symbol else False for x in Board_List[i]]):
                return Symbol
            
    lst=[]
    for i in range(0,3):
        lst=[]
        for j in range(0,3):
            lst.append(Board_List[j][i])
        if all([True if x==Symbol else False for x in lst]):
            return Symbol
        
    lst=[]
    for i in range(0,3):
        lst.append(Board_List[i][i])
    if all([True if x==Symbol else False for x in lst]):
        return Symbol
    
    
    lst=[]
    for i,j in zip(range(0,3),range(2,-1,-1)):
        lst.append(Board_List[i][j])
    if all([True if x==Symbol else False for x in lst]):
        return Symbol
    
    return ""




print("Welcome to tic tac toc game....")
print("The available moves numbers are (1~9) as shown on board squares")
New_Game=True
while(New_Game==True):
    while(True):
        try:
            Player_Symbol='X' if int(input("Please,Select Your Symbol....1 for symbol'X'....Otherwise for symbol 'O'....Your Choice:"))==1 else 'O'
        except:
            print("Invalid input numbers only...")
        else:
            AI_Symbol='X' if Player_Symbol=='O' else 'O'
            break

    Board_List=[[x for x in range(1,4)],[x for x in range(4,7)],[x for x in range(7,10)]]
    Available_Movements=reduce(lambda a,b:a+b,Board_List)
    Draw_Board(Board_List)
    Winner=""
    while len(Available_Movements) != 0:
        Take_Player_Movement(Board_List)
        Winner=Check_Win(Board_List,Player_Symbol)
        if Winner!="":
            break
        if len(Available_Movements) == 0:
            break
        AI_Movement(Available_Movements)
        Winner= Check_Win(Board_List,AI_Symbol)
        if Winner!="":
            break
    if Winner==Player_Symbol:
        print("You Won....","Game Over",sep="\n")
    elif Winner==AI_Symbol:
        print("You lost....","Game Over",sep="\n")        
    else:
        print("Tie....","Game Over",sep="\n")   
    x=input("Play again....? Y to continue Otherwise to exit:")
    New_Game= True if (x).lower()=='y' else False


print("Good Bye...")