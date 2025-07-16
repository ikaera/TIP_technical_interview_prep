'''

U - Understand
    I - Input
    O - Output 
    C - constraints/considerations
    E - example/edge cases
M - Match
P - Plan
    High-level: 

    Steps: 

I - Implement '''

def evaluate_ternary_expression_iterative(expression):
    stack = []
    
    # Traverse the expression from right to left
    for i in range(len(expression) - 1, -1, -1):
        char = expression[i]
        
        # Check if the top of the stack is '?', indicating a ternary operation
        if stack and stack[-1] == '?':
            stack.pop()  # Remove the '?'
            true_expr = stack.pop()  # Pop the true branch expression
            stack.pop()  # Remove the ':' separator
            false_expr = stack.pop()  # Pop the false branch expression
            
            # Evaluate the condition (current character)
            if char == 'T':
                stack.append(true_expr)  # Push true branch result
            else:
                stack.append(false_expr)  # Push false branch result
        else:
            stack.append(char)  # Push non-ternary characters to the stack
    
    # The final result is the only remaining element in the stack
    return stack[0]

def evaluate_ternary_expression_recursive(expression):
    pass

# Example Usage:
print(evaluate_ternary_expression_recursive("T?2:3"))
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))