done = 'n'
while(done == 'n'):
    value = float(input("What is your first number?\n"))
    done = 'y'
    while(done == 'y'):
        print("*\n/\n+\n-")
        operation = input("Pick an operation:")
        new_number = float(input("Pick the next number:"))
        if(operation == '*'):
            print(f"{value} {operation} {new_number} = {value * new_number}")
            value = value * new_number
        elif(operation == '+'):
            print(f"{value} {operation} {new_number} = {value + new_number}")
            value = value + new_number
        elif(operation == '-'):
            print(f"{value} {operation} {new_number} = {value - new_number}")
            value = value - new_number
        else:
            print(f"{value} {operation} {new_number} = {value / new_number}")
            value = value / new_number
        done = input(f"Type \'y\' to continue calculating with {value} or type \'n\' to start a new calculation.\n")
