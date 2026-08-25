def calculator (a:float, b:float, op:str) -> float:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a/b 
    elif op == "%":
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        return a % b
    elif op == "//":
        if b == 0:
            raise ValueError ("Cannot floor-divide by zero")
        return a // b
    elif op == "**":
        result = a ** b
        if isinstance(result,complex):
            raise ValueError(f"Result is a complex number: {result}")
        return result
    else:
        raise ValueError("Invalid operator")

while True:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input("Enter the operator (+,-,*,/,%,//,**): ")

    try:
        print("Result: ",calculator(a,b,op))
    except ValueError as e:
        print("Error: ", e)
    
    answer = input("Continue? (y/n): ").lower()
    if answer not in ("y","yes"):
        break

