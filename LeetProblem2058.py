# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        locations = []
        c = 1
        while head.next and head.next.next:
            prevValue = head.val
            head = head.next
            if (head.val > prevValue and head.val > head.next.val) or (head.val < prevValue and head.val < head.next.val):
                locations.append(c)
            c += 1
        print(locations)
        if len(locations) < 2:
            return [-1,-1]
        distances = [locations[i+1]-locations[i] for i in range(len(locations)-1)]
        print(distances)
        return [min(distances),sum(distances)]
            
        