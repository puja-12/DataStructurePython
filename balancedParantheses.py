def valid_paren(input_str):
    # Declaraing a stack.
    stack = []
    # Iterating over the entire string
    for paren in input_str:
        # If the input string contains an opening parenthesis,
        # push in on to the stack.
        if paren == '(' or paren == '[' or paren == '{':
            stack.append(paren)
        else:
            # In the case of valid parentheses, the stack cannot be
            # be empty if a closing parenthesis is encountered.
            if not stack:
                print(input_str, "contains invalid parentheses.")
                return
            else:
                # If the input string contains a closing bracket,
                # then pop the corresponding opening parenthesis if
                # present.
                top = stack[-1]
                if paren == ')' and top == '(' or \
                        paren == ']' and top == '[' or \
                        paren == '}' and top == '{':
                    stack.pop()
    # Checking the status of the stack to determine the
    # validity of the string.
    if not stack:
        return True
    return False


# Driver Code
if __name__ == "__main__":
    expr = "((5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3))"
    if valid_paren(expr):
        print("Balanced")
    else:
        print("Not Balanced")

