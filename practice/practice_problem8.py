"""
You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.
"""
import re
def checkRecord(s: str) -> bool:

        x = s.find("L")
        for i in range(len(s)-1):
            if "L" in s:
                if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == "L":
                    lates = False
                    break

        if s.count("A") >= 2:
            absents = False

        print(absents)
        print(lates)
        if absents == True and lates == True:
            return True
        else:
            return False


print(checkRecord("LLPPLPPLPLPPLPLPLPPAPPPPPLPALL"))