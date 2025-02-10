# question 1 answer
# Write a Python function that takes a string and returns a dictionary with the count of each unique word. Ignore case and punctuation.
# Example:-
# input_text = "Hello world! Hello Python."
# output = {"hello": 2, "world": 1, "python": 1}

def word_counter(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum() or char.isspace())
    
    # Split into words and count occurrences
    words = cleaned_text.split()
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts


given_text=input() # Hello world! Hello Python.
print(word_counter())


# question 2 answer
# The following function is inefficient. Optimize it for better performance.

# Task: Rewrite the function to reduce time complexity.
# Reduced to O(n)
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            
    return list(duplicates)

sample_test=[1, 2, 3, 4, 5, 3, 2, 6, 7]
print(find_duplicates(sample_test))