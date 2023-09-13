def solution(S):
    caracter_abierto = {'(', '{', '['}
    caracter_cerrado = {')', '}', ']'}
    
    pila = []
    
    for caracter in S:
        if caracter in caracter_abierto:
            pass
            pila.append(caracter)
        elif caracter in caracter_cerrado:
            if not pila:
                return 0
            comparacion = pila.pop()
            if (caracter == ')' and comparacion != '(') or (caracter == '}' and comparacion != '{') or (caracter == ']' and comparacion != '['):
                return 0

    return 1 if not pila else 0

print(solution("{[(u)()]}")) 
print(solution("([)()]"))    