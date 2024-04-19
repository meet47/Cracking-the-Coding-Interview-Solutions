#1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique(string):

    unique_set = set()
    for i in string:
        unique_set.add(i)
    
    if len(string) == len(unique_set):
        return True
    else:
        return False
 
print(is_unique("abcd"))

# TIme Complexity: O(n), where n = Length of the String
# Space Complexity: O(1)



