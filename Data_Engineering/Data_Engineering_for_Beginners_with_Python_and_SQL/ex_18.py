# Count Occurrences of a Word
# Create a function called count_word_occurrences that takes a string and a target word as input and returns the number of times the target word appears 
# in the string. The function should not be case-sensitive, 
# meaning it should count occurrences regardless of the word's case. Your function should use only built-in Python tools.

def count_word_occurrences(text:str, word:str) -> int:
    # Your code here
    if text == "" or word == "":
        return 0

    return text.lower().count(word.lower())


assert count_word_occurrences("The quick brown fox jumps over the lazy dog.", "the") == 2  
# "the" appears twice (both in lowercase and uppercase).

assert count_word_occurrences("This is a test sentence. This sentence is a test.", "sentence") == 2  
# "sentence" appears twice.

assert count_word_occurrences("Python is a versatile programming language.", "Python") == 1  
# "Python" appears once (case-insensitive).

assert count_word_occurrences("No matches here.", "word") == 0  
# "word" does not appear in the text.

assert count_word_occurrences("","") == 0

