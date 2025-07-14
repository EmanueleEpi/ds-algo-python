from week_00_bootup.binary_tree import (TreeNode, inorder, level_order,
                                        postorder, preorder)


def sample_tree():
    # Tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def test_preorder():
    assert preorder(sample_tree()) == [1, 2, 4, 5, 3]


def test_inorder():
    assert inorder(sample_tree()) == [4, 2, 5, 1, 3]


def test_postorder():
    assert postorder(sample_tree()) == [4, 5, 2, 3, 1]


def test_level_order():
    assert level_order(sample_tree()) == [1, 2, 3, 4, 5]
