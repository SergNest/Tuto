result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        user_input = input("> ")
        if user_input == "=":
            break
        elif user_input in ["+", "-", "*", "/"]:
                operator = user_input
                wait_for_number = True
        else:
            num = float(user_input)
            if not wait_for_number:
                print("Error: number already entered.")
            elif operator is None:
                result = num
                wait_for_number = False
            elif operator == "+":
                result += num
                wait_for_number = False
            elif operator == "-":
                result -= num
                wait_for_number = False
            elif operator == "*":
                result *= num
                wait_for_number = False
            elif operator == "/":
                result /= num
                wait_for_number = False
    except ValueError:
        print(f"Error: '{user_input}' is not a number. Try again.")







        
        
