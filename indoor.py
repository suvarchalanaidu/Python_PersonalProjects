#Program in Python that prompts the user for input and then outputs that same input in lowercase. 
#Punctuation and whitespace should be outputted unchanged.

inputstring = input("Enter your text in upper case: ")

if(inputstring.isupper()):
    outputstring = str.lower(inputstring)
    print(outputstring)
else:
    print("enter string in upper case only")