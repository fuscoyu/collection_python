import json
# coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(0)
        r = ret
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10 #表示进位
            r.next = ListNode(s%10) #指向下一个元素 0->7
            r = r.next # 将r指向下个下个元素 
            if l1: l1 = l1.next 
            if l2: l2 = l2.next
        if carry > 0:
            r.next = ListNode(1)
        return ret.next

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:# C^d可以跳出输入
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print (out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
