import queue

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
        # print(node.val)
        # print(node.left)
        return node
    return helper(0)
#=================================================================================
def printTree(node):

    
    # thislevel = [node] 
    # print('[',end="")
    # while thislevel:
    #     nextlevel = list() 
    #     print('[',end="")
    #     for n in thislevel:
    #     #   print(thislevel)  
    #         print(n.val,end="")
    #         if n.left: nextlevel.append(n.left)
    #         if n.right: nextlevel.append(n.right)
    #     print(']',end="")
    #     thislevel = nextlevel
    # print(']')


    thislevel = queue.Queue(node)
    print(thislevel.qsize())
    while thislevel:
        nextlevel = queue.Queue()
        # for n in thislevel.:
        #     print(n.val)


    # q = queue.Queue()
    # print(type(q))

    # if node.val != None:
    #     q.put(node.val)
    #     # q.get()
    #     print(q.get(),end=" ")
    #     if node.left != None:
    #         printTree(node.left)
    #     if node.right != None:
    #         printTree(node.right)
    # else : 
    #     return 

# 위에 코드는 dfs로 작성한것 

    
    # print(q.get())
    # all_lines = []
    # return all_lines

def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    # print(type(node))
    # print(node)
    # for i in range(len(node)):
    #     print(node[i].value,end="")

    printTree(node)
    # print(printTree(node)) # [[1], [2, 3], [4, 5, 6, 7]]

if __name__ == "__main__":
    main()
    