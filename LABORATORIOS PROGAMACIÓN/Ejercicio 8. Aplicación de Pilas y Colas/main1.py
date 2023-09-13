def solution(S):

    caracter_symbols = {')': '(', '}': '{', ']': '['}

    # Inicializar una pila vacía
    stack = []

    # Recorrer la cadena de entrada
    for char in S:
        if char in caracter_symbols.values():
            stack.append(char)
        elif char in caracter_symbols.keys():
            if not stack:
                return 0
            top = stack.pop()
            if caracter_symbols[char] != top:
                return 0
        else:
            return 0

    # Al final, verificar si la pila está vacía
    return 1 if not stack else 0

# Pruebas
print(solution("{[(u)(ae)]}"))  # Output: 1
print(solution("([)()]"))    # Output: 0
