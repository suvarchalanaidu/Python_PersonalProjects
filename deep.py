#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, 
#the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
# Otherwise output No.


answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")
#uncomment below if you want to use if-elif
#if(answer == "42"):
#    print("Yes")
#elif(answer == "forty-two"):
#    print("Yes")
#elif(answer == "forty two"):
#    print("Yes")
#else:
#    print("Guess again")

#below is by using match-case
match(answer):
    case "forty-two" | "forty two" | "42":
        print("Yes")
    case _:
        print("No")