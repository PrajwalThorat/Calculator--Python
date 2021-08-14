print("Welcome to calculator ")

while True:
    print("Option :-")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplicaton")
    print("4.Divison")
    print("5.Exit")
    user_input = input(": ")

    if user_input == "5":
        print("Exit Calculator")
        break

    elif user_input == "1":
        a = float(input("Enter the 1st number:"))
        b = float(input("Enter the 2nd numbe to add:"))
        result = a + b
        print(result)
    
    elif user_input == "2":
        a = float(input("Enter the 1st number:"))
        b = float(input("Enter the 2nd numbe to sub:"))
        result = a - b
        print(result)
    
    elif user_input == "3":
        a = float(input("Enter the 1st number:"))
        b = float(input("Enter the 2nd numbe to mul:"))
        result = a * b
        print(result)
    
    elif user_input == "4":
        a = float(input("Enter the 1st number:"))
        b = float(input("Enter the 2nd numbe to Div:"))
        result = a / b
        print(result)

    else:
        print("Enter the valid number")
           
        
