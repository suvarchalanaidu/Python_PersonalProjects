#In a file called bank.py, implement a program that prompts the user for a greeting. 
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. 
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

#way 1
greeting = input("Please provide a greeting: ")

def main():
    startstringcheck = greeting[:5]
    startcharcheck = greeting[:1]

    if(startstringcheck.lower() == "hello"):
        print("$0")
    elif(startcharcheck.lower() == "h"):
        print("$20")
    else:
        print("$100")
main()

#way 2
#def main():
#    greet = input("Greetings! \n").strip().lower()
#    if greet.startswith("h"):
#        if greet.startswith("hello"):
#            print("$0")
#        else:
#            print("$20")
#    else:
#        print("$100")


#main()