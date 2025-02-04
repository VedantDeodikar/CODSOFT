while True:
    print("\nWelcome to the simple calculator!")
    print("Choose an operation:")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    operation = input("Enter the operation (1, 2, 3, 4 or 5): ")
    if operation == '1':
        num1=int(input("Enter first no:"))
        num2=int(input("Enter second no:"))
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is: {result}")
    elif operation == '2':
        num1=int(input("Enter first no:"))
        num2=int(input("Enter second no:"))
        result = num1 - num2
        print(f"The result of subtracting {num1} and {num2} is: {result}")
    elif operation == '3':
        num1=int(input("Enter first no:"))
        num2=int(input("Enter second no:"))
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is: {result}")
    elif operation == '4':
        num1=int(input("Enter first no:"))
        num2=int(input("Enter second no:"))
        if num2 != 0:
            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is: {result}")
        else:
            print("Error! Division by zero is not allowed.")
    elif operation == '5':
        print("Exiting...")
        break
    else:
        print("Invalid operation! Please choose a valid operation (1, 2, 3, or 4).")
        continue
