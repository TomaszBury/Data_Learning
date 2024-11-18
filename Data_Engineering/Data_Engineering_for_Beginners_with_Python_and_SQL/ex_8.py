# Check Palindrome
# Write a function called is_palindrome that takes a string as an argument and returns True 
# if it's a palindrome, and False otherwise. 
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backward as forwards, 
# such as madam or racecar.

def is_palindrome(string:str) -> bool:
    '''
     Function called is_palindrome that takes a string as an argument and 
     returns True if it's a palindrome, and False otherwise.

     :param: string: str: -any string
     :return bool: True if it's a palindrome, and False otherwise.
    '''
    if isinstance(string, str) and string == string[::-1]:
        return True

    return False

assert is_palindrome("madam") == True
assert is_palindrome("racecar") == True
assert is_palindrome(9) == False
assert is_palindrome("The variable is a string") == False