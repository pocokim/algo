
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
        if node.left == None and node.right == None:
            print(node.val)
            cur_path.append(node.val)
            print(cur_path)
            print(all_paths)
            all_paths.append(cur_path)
            print(all_paths)
            cur_path.pop()
            print(all_paths)
            # cur_path 에는 [1,2,4]가 들어가있었다. 그리고 이걸 all_path에 추가해주었다. 그리고 cur_path의 마지막원소를 뺐는데... 이 과정으로 all_path에 추가되어있던 값도 빠져버렸다. 
            

        else:
            cur_path.append(node.val)
            print(cur_path)
            dfsHelper(node.left,cur_path)
            dfsHelper(node.right,cur_path)

        # 이 코드의 문제점 : 1) cur_path를 수정해버리면, all_path 까지 바뀌어버린다.  2) 2가 안빠진다. 
        # 내가 생각하는 해결책 :
        # 1) 이러한 문제점을 해결해주기 위해서 return 을 사용해야할것같다. cur_path 가 계속 전달되기 때문이다.   
        # 2) cur_path를 바로 넣어주는것이 아니라 값만 넣어주기 위해서 새로운 변수를 만들어야할것같다. 

        # none노드일때 처리하는게 더 예쁠것같아서 none 일때로 조건을 잡았는데  left , right에 대해서 2번씩 실행되어서 리프노드일때 처리하는것으로 바꿈 
        # if node == None :
        #     all_paths.append(cur_path)
        #     cur_path.pop()
        #     return 
            # return cur_path 

        # cur_path.append(node.val)
        # print(cur_path)
        # print(all_paths)
        # leftPath = dfsHelper(node.left,cur_path)
        # rightPath = dfsHelper(node.right,cur_path)
        # # return

    dfsHelper(node, [])
    return all_paths
    
def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    printTree(node)
    print(all_paths(node))

if __name__ == "__main__":
    main()
    