def rpn_calculate(expression):
    array = []
    params = expression.split()
    
    for param in params:
        if param in "+-*":
            # Assurez-vous que la pile a au moins deux nombres pour effectuer l'opération
            if len(array) < 2:
                raise ValueError("Insufficient values in the expression.")
            # Récupérez les deux derniers nombres
            num2 = array.pop()
            num1 = array.pop()
            
            if param == '+':
                array.append(num1 + num2)
            elif param == '-':
                array.append(num1 - num2)
            elif param == '*':
                array.append(num1 * num2)
        else:
            # Assurez-vous que le param est un nombre valide
            try:
                num = float(param)
                array.append(num)
            except ValueError:
                raise ValueError(f"Invalid param: {param}")
    
    if len(array) != 1:
        raise ValueError("The user input has too many values.")
    
    return array.pop()

# Exemple d'utilisation
expressions = [
    "3 4 +",         # 7
    "3 4 + 5 *",     # 35
    "5 1 2 + 4 * + 3 -"  # 14
]

for expr in expressions:
    result = rpn_calculate(expr)
    print(f"Result of '{expr}': {result}")
