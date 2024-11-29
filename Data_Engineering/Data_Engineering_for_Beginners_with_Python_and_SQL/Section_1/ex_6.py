# Reverse a String
# Create a function called reverse_string that takes a string 
# as input and returns a new string with its characters reversed. 
# Your function should use only built-in Python tools.
# 

def reverse_string(input_string:str) -> str:
    '''
    Revess string

    :param input_string:str: any string 
    :return str: reversed string
    '''
    # Your code here
    return input_string[::-1]

in_test_first:str = "Hello, World!"
out_test_first:str = "!dlroW ,olleH"

assert reverse_string(in_test_first) == out_test_first

in_second:str = "Python"
out_second:str = "nohtyP"

assert reverse_string(in_second) == out_second

in_third:str = ""
# out_third:str = ""

assert reverse_string(in_third) == in_third