# Problem Link ---> https://leetcode.com/problems/reverse-words-in-a-string/description/

# Problem Statement ---> Given an input string s, reverse the order of the words.
"""
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""
# Approach --> Backward Traversal
"""
--Start from the end of the string.
--Skip any spaces.
--Mark the end of a word and move left until a space is found.
--Extract the word and add it to a result list.
--Repeat until the beginning of the string is reached.
--Finally, join all words with a single space and return the result.
"""
# Time Complexity --> O(n)
# Space Complexity --> O(n)


class Solution:

  def reverseWords(self, s: str) -> str:
    if len(s) == 0:
      return ""
    ans = []
    end = len(s) - 1
    while end >= 0:
      # skip trailing spaces
      while end >= 0 and s[end] == ' ':
        end -= 1

      if end < 0:
        break

      # find start of the word
      start = end
      while end >= 0 and s[end] != ' ':
        end -= 1

      # add word to res

      ans.append(s[end + 1:start + 1])

    return " ".join(ans)


if __name__ == "__main__":
  sol = Solution()
  print(sol.reverseWords("the sky is blue"))  # "blue is sky the"
  print(sol.reverseWords("  hello world  "))  # "world hello"
  print(sol.reverseWords("a good   example"))  # "example good a"
  print(sol.reverseWords(
      "Alice does not even like Bob"))  # "Bob like even not does Alice"
