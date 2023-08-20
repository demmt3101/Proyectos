def solution(S):
    # Inicializar una pila vacía
    stack = []

    # Recorrer la cadena de entrada
    for char in S:
        if char in '({[':
            # Si el carácter es un símbolo de apertura, agregarlo a la pila
            stack.append(char)
            print(stack)
        else:
            # Si el carácter es un símbolo de cierre, verificar si coincide con el elemento superior de la pila
            if not stack:
                return 0
            top = stack.pop()
            if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                return 0
            print(stack)
            
    # Al final, verificar si la pila está vacía
    return 1 if not stack else 0

# Pruebas
print(solution("{[()()]}"))  # Output: 1
print(solution("([)()]"))    # Output: 0
