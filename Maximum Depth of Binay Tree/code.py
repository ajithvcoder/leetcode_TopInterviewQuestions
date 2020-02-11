"""

input : binary tree [3,9,20,null,null,15,7]
output : 3


"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        nodeStack=[root]
        depthStack=[1]
        maxDepth=0
        while len(nodeStack)>0:
            node=nodeStack.pop()
            depth=depthStack.pop()
            maxDepth=maxDepth if maxDepth>depth else depth
            if node.left!=None:
                nodeStack.append(node.left)
                depthStack.append(depth+1)
            if node.right!=None:
                nodeStack.append(node.right)
                depthStack.append(depth+1)
        return maxDepth
