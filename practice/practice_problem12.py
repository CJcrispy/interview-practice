"""
Your friend is typing his name into a keyboard. 
Sometimes, when typing a character c, the key might get long pressed, 
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. 
Return True if it is possible that it was your friends name, 
with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

"""

def isLongPressedName(name: str, typed: str) -> bool:

    i = 0
    for j in range(len(typed)):
        """
        in each iteration of the for loop we are checking if the length of name is greater than
        our first pointer and comparing the characters in the strings
        """
        if i < len(name) and name[i] == typed[j]:
            i += 1
        elif j == 0 or typed[j] != typed[j - 1]:
            return False
    return i == len(name)

print(isLongPressedName(name = "alex", typed = "aaleex"))
print(isLongPressedName(name = "saeed", typed = "ssaaedd"))
print(isLongPressedName(name = "leelee", typed = "lleeelee"))
print(isLongPressedName(name = "laiden", typed = "laiden"))