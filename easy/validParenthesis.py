# Problem Link ---> https://leetcode.com/problems/valid-parentheses/description/

# Problem Statement ---> Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# Approach --> Using Stack
# Initialize an empty stack.
# Traverse the string character by character:
# --If the character is an opening bracket ((, {, [), push it onto the stack.
# --If the character is a closing bracket (), }, ]):
# ----Check if the stack is not empty and the top of the stack is the corresponding opening bracket.
# ----If yes → pop from the stack.
# ----If no → return False (mismatch found).
# After traversal:
# If the stack is empty → return True (all brackets matched).
# Otherwise → return False (some opening brackets were not closed).

# Time Complexity --> O(n)
# Space Complexity --> O(n)

class Solution:
  def isValid(self, s: str) -> bool:
      stack = []
      for char in s:
          if char in "({[":
              stack.append(char)
          else:
              if (len(stack) > 0) and ((stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']')):
                  stack.pop()
              else:
                  return False
      return True if len(stack) == 0 else False

# 
if __name__ == "__main__":
  sol = Solution()
  print(sol.isValid("()"))        # True
  print(sol.isValid("()[]{}"))    # True
  print(sol.isValid("(]"))        # False
  print(sol.isValid("([)]"))      # False
  print(sol.isValid("{[]}"))      # True

