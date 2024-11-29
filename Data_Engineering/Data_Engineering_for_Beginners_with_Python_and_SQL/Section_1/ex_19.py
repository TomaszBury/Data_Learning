# Check Balanced Parentheses
# Create a function called is_balanced_parentheses that takes a string containing only parentheses, brackets, 
# and curly braces as input and returns True if the parentheses are balanced and False otherwise. 
# The parentheses are considered balanced if they are closed in the correct order. Your function should use only built-in Python tools.

def is_balanced_parentheses(s: str) -> bool:
    """
    Check if the given string of parentheses, brackets, and curly braces is balanced.

    Args:
    s (str): The input string containing only '()', '[]', and '{}'.

    Returns:
    bool: True if the string is balanced, False otherwise.
    """
    # Dictionary to hold matching pairs
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    
    # Stack to keep track of opening characters
    stack = []
    
    for char in s:
        if char in matching_pairs.values():
            # If it's an opening character, push to stack
            stack.append(char)
        elif char in matching_pairs.keys():
            # If it's a closing character, check for matching opening character
            if stack == [] or matching_pairs[char] != stack.pop():
                return False
        else:
            # If an unexpected character is found
            return False
    
    # If stack is empty, all characters matched correctly
    return stack == []


assert is_balanced_parentheses("()") == True
assert is_balanced_parentheses("()[]{}") == True
assert is_balanced_parentheses("(]") == False
assert is_balanced_parentheses("([)]") == False
assert is_balanced_parentheses("{[]}") == True
