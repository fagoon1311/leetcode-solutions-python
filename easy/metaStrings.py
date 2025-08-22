# Check if One String Swap Can Make Strings Equal --> https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

# Problem Statement ---> You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

# Approach --> Two Pointers
"""
--If the strings are equal, return true.
--If the strings are not equal, check if they are of equal length.
--If they are not of equal length, return false.    
--If they are of equal length, check if they are meta strings.
--If they are meta strings, return true.
--If they are not meta strings, return false.

"""
# Time Complexity --> O(n)
# Space Complexity --> O(1)

def checkMeta(str1, str2):
  if len(str1) != len(str2):
      return False
  if str1 == str2:
      return True

  diff = 0
  p1 = 0
  while p1 < len(str1):
      print(diff)
      if str1[p1] != str2[p1]:
          diff += 1
          p1 += 1
      else:
          p1 += 1

  print(diff)
  return diff == 2


checkMeta("Coding", "Codnig")


