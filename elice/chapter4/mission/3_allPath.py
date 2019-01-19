
#====이 문제를 풀기 위해 필요한 클래스와 함수들입니다. 따로 수정 할 필요는 없습니다.
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def listToCompleteBinaryTree(lst):
    def helper(index):
        if index >= len(lst):
            return None
        node = Node(lst[index])
        node.left = helper(index * 2 + 1)
        node.right = helper(index * 2 + 2)
        return node
    return helper(0)

def printTree(node):
    q = [Node(-1), node]

    line = []
    while q:
        node = q.pop()
        if not node:
            continue
        elif node.val == -1:
            if len(line) > 0:
                print(" ".join(line))
                line = []
                q.insert(0,Node(-1))
        else:
            q.insert(0,node.left)
            q.insert(0,node.right)
            line.append(str(node.val))
#=================================================================================
def all_paths(node):
    all_paths = []
    def dfsHelper(node, cur_path):
        # 여기에 깊이 우선 탐색을 구현 해 봅시다.
        return
    dfsHelper(node, [])
    return all_paths
    
def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    printTree(node)
    print(all_paths(node))

if __name__ == "__main__":
    main()
    