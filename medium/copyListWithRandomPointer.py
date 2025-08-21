# Problem Link ---> https://leetcode.com/problems/copy-list-with-random-pointer/description/

# Problem Statement ---> A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null. Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# Approach1  --> Using HashMap
"""
--Create a hashmap to store the mapping of old nodes to new nodes.
--Traverse the original list and create new nodes for each old node.
--Store the mapping of old nodes to new nodes in the hashmap.
--Traverse the original list again and set the next and random pointers of the new nodes using the hashmap.
--Return the head of the new list.
"""
# Time Complexity --> O(n)
# Space Complexity --> O(n)  



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        add = {None: None}
        temp = head
        while temp != None:
            newNode = Node(temp.val)
            add[temp] = newNode
            temp = temp.next

        temp = head
        while temp != None:
            copyNode = add[temp]
            copyNode.next = add[temp.next]
            copyNode.random = add[temp.random]
            temp = temp.next

        return add[head]



# Approach2  --> Without Using HashMap
"""
--Insert Copy nodes in between.
--Connecting Random Pointers
--Connecting the next pointers/Extracting the list
"""

class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      # Insert Copy nodes in between.
      temp = head
      while temp != None:
          copyNode = Node(temp.val)
          copyNode.next = temp.next
          temp.next = copyNode
          temp = temp.next.next

      # Connecting Random Pointers
      temp = head
      while temp != None:
          copyNode = temp.next
          copyNode.random = temp.random.next if temp.random else None
          temp = temp.next.next

      # Connecting the next pointers/Extracting the list
      dummy = Node(-1)
      res = dummy
      temp = head
      while temp != None:
          res.next = temp.next
          temp.next = temp.next.next
          res = res.next
          temp = temp.next

      return dummy.next