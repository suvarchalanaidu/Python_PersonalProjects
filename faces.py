#implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 
# (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). 
# All other text should be returned unchanged.
def convert(txtinp):

    outputstring = txtinp.replace(":)", "\U0001F642").replace(":(","\U0001F641")

    print(outputstring)
    return outputstring 

def main():
    userinput = input("Enter any text with :) or :(  included: ")
    print(userinput)
    convert(userinput) 

main()       