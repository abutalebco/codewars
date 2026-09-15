def evaluate(equation):
    tokens = [int(x) for x in equation.replace(" ", "").split('@')]
    
    result = tokens[0]
    
    for next_num in tokens[1:]:
        if next_num == 0:
            return None
        add = result + next_num
        sub = result - next_num
        mul = result * next_num
        fdiv = result  // next_num
        
        result = add + sub + mul + fdiv
    
    return result