# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        l = []
        d = deque()
        d.append(root)
        while len(d) > 0:
            r = d.pop()
            
            mid_val = r.val
            left_root = r.left
            if left_root is not None:
                d.append(left_root)
                while left_root.right is not None:
                    left_root = left_root.right

                if left_root.val > mid_val:
                    l.append(left_root)
                    l.append(r)
                    if len(l) == 4:
                        break
            right_root = r.right
            if right_root is not None:
                d.append(right_root)
                while right_root.left is not None:
                    right_root = right_root.left

                if mid_val > right_root.val:
                    l.append(r)
                    l.append(right_root)
                    if len(l) == 4:
                        break

        
        if len(l) == 2:
            l[0].val, l[1].val = l[1].val, l[0].val
        else:
            if l[0].val > l[2].val:
                l[0].val, l[3].val = l[3].val, l[0].val
            else:
                l[1].val, l[2].val = l[2].val, l[1].val

        return root
            
            
        