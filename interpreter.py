#Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result 
#as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, 
#with one space between x and y and one space between y and z

userinp = (input("Enter an arithmetic expression: "))

x, y , z = (userinp.split(" ")) #converts to list

match(y):
    case '+':
        result =  int(x) + int(z)
    case '-':
        result =  int(x) - int(z)
    case '*':
        result =  int(x) * int(z)
    case '/':
        result =  int(x) / int(z)
    
    case _:
        print("Enter Valid expression")

floatnumer =  (float(result))
output = round(floatnumer,1)

print(output)