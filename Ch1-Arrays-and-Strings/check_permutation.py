#1.2 Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    
    if sorted(string1) == sorted(string2):
        return True
    
    return False

print(is_permutation("abcd", "bdca"))

#Time Complexity: O(nlong) Since we're sorting the string
#Space Complexity: O(n) Since sorting takes additional space to sort the 

#Optimal Approach

def is_permutation_2(string1, string2):
    if len(string1) != len(string2):
        return False
    
    char_dict = {}

    for i in string1:
        char_dict[i] = char_dict.get(i, 0) + 1

    for i in string2:
        if i not in char_dict or char_dict[i] == 0:
            return False
        char_dict[i] -= 1

    for i in char_dict.values():
        if i != 0:
            return False
        
    return True

print(is_permutation_2("abcd", "bdca"))

#Time Complexity: O(n) Since we're sorting the string
#Space Complexity: O(n) Since sorting takes additional space to sort the 