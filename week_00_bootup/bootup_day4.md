## Boot-Up Day 4 (Thu, Jul 3)

### Topics Covered
- Binary Trees: structure, nodes, traversal patterns
- DFS: Preorder, Inorder, Postorder (recursive)
- BFS: Level-order

### Key Insights
- Preorder good for copying trees, Postorder for deleting
- Inorder gives sorted result for BSTs
- Level order uses a queue; recursion can't do it cleanly

### Code Added
- `binary_tree.py` with `TreeNode` and traversal functions

### Tests
- Built sample tree (1,2,3,4,5)
- Verified all traversal outputs using `pytest`
- Passed pre-commit formatting hooks

### GitHub
[commit-link]
