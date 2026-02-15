import random
row1= [' ', ' ', ' ']
row2= [' ', ' ', ' ']
row3= [' ', ' ', ' ']

def program_completed():
        if row1[0]=='X' and row1[1]=='X'and row1[2]=='X':
            print("You won!!")
            return True
        
            

        elif row2[0]=='X' and row2[1]=='X'and row2[2]=='X':
            print("You won!!")
            return True
            

        elif row3[0]=='X' and row3[1]=='X'and row3[2]=='X':
            print("You won!!")
            return True
            

        elif row1[2]=='X' and row2[1]=='X'and row3[0]=='X':
            print("You won!!")
            return True

        elif row1[0]=='X' and row2[1]=='X'and row3[2]=='X':
            print("You won!!")
            return True
        
        elif row1[0]=='X' and row2[0]=='X' and row3[0]=='X':
            print("You won!!")
            return True

        elif row1[1]=='X' and row2[1]=='X' and row3[1]=='X':
            print("You won!!")
            return True

        elif row1[2]=='X' and row2[2]=='X' and row3[2]=='X':
            print("You won!!")
            return True


        elif row1[0]=='O' and row1[1]=='O'and row1[2]=='O':
            print("Programmer won!!")
            return True
            

        elif row2[0]=='O' and row2[1]=='O'and row2[2]=='O':
            print("Programmer won!!")
            return True
            

        elif row3[0]=='O' and row3[1]=='O'and row3[2]=='O':
            print("Programmer won!!")
            return True
            

        elif row1[2]=='O' and row2[1]=='O'and row3[0]=='O':
            print("Programmer won!!")
            return True

        elif row1[0]=='O' and row2[1]=='O'and row3[2]=='O':
            print("Programmer won!!")
            return True
            
        elif row1[0]=='O' and row2[0]=='O' and row3[0]=='O':
            print("Programmer won!!")
            return True

        elif row1[1]=='O' and row2[1]=='O' and row3[1]=='O':
            print("Programmer won!!")
            return True

        elif row1[2]=='O' and row2[2]=='O' and row3[2]=='O':
            print("Programmer won!!")
            return True
        

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)



def user_input(row,index):
    if row == 1:
        row1[index]='X'
    elif row == 2:
        row2[index]='X'
    else:
        row3[index]='X'
      

def programmer():
    print("Now its my turn! ")
    while True:
        random_row= random.randint(1,3)
        random_index= random.randint(0,2)
        
        if random_row == 1 and row1[random_index]== ' ':
            row1[random_index]='O'
            break
            


        elif random_row == 2 and row2[random_index]== ' ':
            row2[random_index]='O'
            break

        elif random_row == 3 and row3[random_index]== ' ':
            row3[random_index]='O'
            break

    
   
    

game_completed=False
tries=0
print("Wanna Play Tic Tac Toe ?? If YES choose the position to add the X and i will add O ")
display(row1,row2,row3)

while game_completed != True:

    while True:
        row= int(input("Choose a row (1-3): "))
        if 1<= row <=3:
            break
        print("Invalid row number!!")   
    
    while True:
        index= int(input("Choose a index (0-2): "))
        if 0<= index <=2:
            break
        print("Invalid index number!!")

    
    if row == 1:
        selected_row = row1
    elif row == 2:
        selected_row = row2
    else:
        selected_row = row3


    while selected_row[index] != ' ':
        print("Cell already filled! Choose another index.")
        index = int(input("Choose a new index (0-2): "))

    

        
    user_input(row,index)
    tries+=1
    display(row1, row2, row3)
    if tries>=5 and program_completed():
        break
    elif tries ==9:
        print("Its a draw!!")
        break
    
    programmer()
    display(row1,row2,row3)
    tries+=1

    if program_completed():
        break
    elif tries==9:
        print("It's a Draw!!")
        break
        

    
   