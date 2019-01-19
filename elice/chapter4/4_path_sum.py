# TIL
# 1.true, false 판단은 마지막에 한번만
# 2.마지막을 만나기전까지 참거짓을 담을 수 있도록(또는 마지막에서 연산되는 참거짓을 담아올 수 있도록 )  isLeft, isRight라는 변수를 만들어 dfsHelper를 실행


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
                print(",".join(line))
                line = []
                q.insert(0,Node(-1))
        else:
            q.insert(0,node.left)
            q.insert(0,node.right)
            line.append(str(node.val))
#=================================================================================
def path_sum(node, targetSum):
    def dfsHelper(node, curSum):
        if node  == None:
            if curSum == targetSum: 
                return True
            else : 
                return False

        curSum += node.val
        print(curSum)
        isLeft = dfsHelper(node.left,curSum)
        isRight = dfsHelper(node.right,curSum)
        return isLeft or isRight

    # true, false를 저장할 수 있는공간이 필요하다. 따라서 단순히 아래와 같이 코드를 작성하는것이 아니라 
        # dfsHelper(node.left,curSum)
        # dfsHelper(node.right,curSum)

        # isRight, isLeft와 같은 변수를 만들었다.
        # 사실 dfsH(node,0)의 결과값이 true,false를 리턴하므로 이런 참거짓판단을 저장할 변수를 만든다는 생각을 하기가 쉽지않다.

        # 큰 맥락에서 봤을때 dfsH(node,0)이 참거짓을 리턴하므로 왼쪽에서 참거짓이 있는지, 또 오른쪽에서 참거짓이 있는지를 저장하자! 라고 생각해서 변수를  초장부터 만들 생각을 하면 너무 좋은것같다.

        # dfsHelper에서 있는지 없는지? 를 dfs(루트노드,0) 은 dfs(2노드,1) 에 있는지 없는지 
        # 즉 각각 dfsHelper(node,0)에서 dfsHelper(Node(2),1) dfsHelper(Node(3),1)이 호출되더라도 서로 다른 함수라는것이다.  

    # dfsHelper(node,0)
    return dfsHelper(node,0)

    # 나의 시행착오 
    #     # 풀이를 떠오른 테크닉 
    #     # 처음에 어떻게 풀까 고민을 했는데, curSum이 계속 전달되고 노드의 위치가 계속 변경되어야한다고 생각했다. 
    #     # 기본적인 dfs 코드의 뼏를 암기하니까 있을때 doS , 끝을만났을떄 doS만 정해주면 되서 코드를 작성하기 편했던것같다. 

    #     if not node :
    #         return 
    #         # 노드가 끝을 만났으므로 종료 

    #         # 궁금한점 1) continue 왜 안되지? - > 애초에 반복문을 도는게 아니기 때문 , 여기서는 return 을 사용하는게 맞음
    #         print('리프노드임')



    #     else :
    #         curSum += node.val 
    #         # print(curSum)

    #         if curSum == targetSum:
    #             print(True)
    #             return True
    #         else : 
    #             dfsHelper(node.left , curSum)
    #             dfsHelper(node.right, curSum)


    # dfsHelper(node, 0) # 찾으면 return True를 해주는것 
    
    # 문제점 
    # 재귀적으로 합을 계산하는것까지는 했는데, true와 false를 어떻게 리턴하거나 출력할지 모르겠다. 
    # curSum이랑 targetSum을 찾았을떄 return True를 해도 , 그 dfsHelper() 를 벗어나는것이지 그러면 그 옆의 dfsHelper()나, 또 상위의 dfsHelper 를 실행하여야하는것이지 않나? 

    # 내가 생각한 해결책, dfsHelper(node,0)으로 찾으면 true를 출력하거나 true를 계속 위로 전달시켜 return true가 반환되고 , 그게 아니면 path_sum함수에서 자체적으로 return False를 해주기.

    # 피드백 
    # 해설을 보니 true, false파악을 리프노드에 왔을때 해주었다. 각 dfsHelper를 재귀적으로 실행할때마다 true, false를 따지는게 아니라 마지막에 도달했을때 한번만 따지면 되서 그게 더 좋은것같다.
    # true,false판단은 마지막에 한번만하고, 그전에는 계속 끝을 만날때까지 전달하도록 left와 right라는 변수를 통해 재귀함수를 전달! 



def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    printTree(node)
    print(path_sum(node, 8)) # return True
    print(path_sum(node, 15)) # return False

if __name__ == "__main__":
    main()
    