# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        def get_levels(tree_node):
            if tree_node is None:
                return([], [])
            else:
                l1_sum, l1_len = get_levels(tree_node.left)
                l2_sum, l2_len = get_levels(tree_node.right)
                len_l1 = len(l1_sum)
                len_l2 = len(l2_sum)
                n = max(len_l1, len_l2)
                out_sum = [0.]*(n+1)
                out_len = [0.]*(n+1)
                for i in range(n):
                    if len_l1 > i:
                        out_sum[i+1] += l1_sum[i] 
                        out_len[i+1] += l1_len[i]
                    if len_l2 > i:
                        out_sum[i+1] += l2_sum[i] 
                        out_len[i+1] += l2_len[i]
                out_sum[0] = tree_node.val
                out_len[0] = 1.
                return(out_sum, out_len)
            
        l_sum, l_len = get_levels(root)
        out = [0.]*len(l_sum)
        for i in range(len(l_sum)):
            out[i] = l_sum[i]/l_len[i]
        return out