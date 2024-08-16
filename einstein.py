#implement a program in Python that prompts the user for mass as an integer (in kilograms) 
#and then outputs the equivalent number of Joules as an integer.

import math

def main():
    massinput = int(input("Enter the mass in kg: "))
    c = 300000000 
    energy = massinput * math.pow(c,2)
    energy=f'{energy:.2f}' #supress the scientific notation
    print(energy)

main()