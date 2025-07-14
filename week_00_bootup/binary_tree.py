from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def preorder(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def level_order(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    q = [root]
    result = []
    while q:
        node = q.pop(0)
        result.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return result
