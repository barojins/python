from typing import Optional


class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        # Sentinel nodes (dummy head and tail)
        # It simplifies edge cases like adding to empty list
        self.head = Node(0)
        self.tail = Node(0)
        # connect head and tail intially
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper function to retrieve a specific node object
    def _get_node(self, index: int) -> Node:
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail            
            for _ in range(self.size - index):
                curr = curr.prev
        return curr

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self._get_node(index)
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        
        if index < self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        node = Node(val)
        node.prev = pred
        node.next = succ
        pred.next = node
        succ.prev = node
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        node = self._get_node(index)
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
