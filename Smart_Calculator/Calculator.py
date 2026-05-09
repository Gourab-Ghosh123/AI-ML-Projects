print("Welcome to Smart Calculator :")
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

operation = input("Choose 1 : Sum , 2 :Substraction , 3 : Multiplication , 4 : Division")

def op(operation):
    match operation:
        case 1 : 
            sum = num1 + num2
            print(sum)

        case 2:
            substraction = num1 - num2
            print(substraction)

        case 3:
            multiplication = num1 * num2
            print(multiplication)

        case 4:
            division = num1 / num2
            print(division)
        
        case _:
            print("Invalid Operation")














