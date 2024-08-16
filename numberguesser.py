import random as rd

running =   True
MaxRange = int(input("Enter the max range: "))
number = rd.randint(1,MaxRange + 1) # +1 because the randint in random library value from 1 through 9 if Maxrange is 10

while(running):

    guessnumber = int(input("Guess the number: "))
    if(guessnumber == number):
        print("You are right!")
        running= False
        break

    elif(guessnumber < number):
        print("Guess a higher number")
    
    elif(guessnumber<number):
        print("Guess a lower number")


