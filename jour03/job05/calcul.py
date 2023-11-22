def calcul(num1, operator, num2):

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    
result1 = calcul(10, '+', 5)
result2 = calcul(10, '-', 5)
result3 = calcul(10, '*', 5)
result4 = calcul(10, '/', 5)

print(result1)
print(result2)
print(result3)
print(result4)
