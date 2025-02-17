def calculate_expression(expression):
    parts = expression.split()
    num1 = int(parts[0])
    op1 = parts[1]
    num2 = int(parts[2])
    op2 = parts[3]
    num3 = int(parts[4])
    if op1 == '*' or op2 == '*':
        if op1 == '*':
            result = num1 * num2
            if op2 == '+':
                result += num3
            elif op2 == '-':
                result -= num3
            elif op2 == '*':
                result *= num3
            else:
                raise ValueError("無效的運算符")
        elif op2 == '*':
            result = num2 * num3
            if op1 == '+':
                result = num1 + result
            elif op1 == '-':
                result = num1 - result
            elif op1 == '*':
                result = num1 * result
            else:
                raise ValueError("無效的運算符")
    else:
        if op1 == '+':
            result = num1 + num2
        elif op1 == '-':
            result = num1 - num2
        else:
            raise ValueError("無效的運算符")
        if op2 == '+':
            result += num3
        elif op2 == '-':
            result -= num3
        else:
            raise ValueError("無效的運算符")

    return result
expression = input()
result = calculate_expression(expression)
print(result)
