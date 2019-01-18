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
        return node

        # helper 함수는 값을 넣고, left와 right에 들어올 노드를 연결해주는 함수이다. 
        # 리스트 클래스에서도 선언하였듯, 위치를 가리키기 위해서는 left나 right에 담기는 것이 val과 같은 값이 아니라 '노드'와 같은 클래스가 담겨야한다.
        # 여기에서는 node.left = '노드' 라고 선언하기보다는 helper함수를 통해 값을 담으면서도, 왼쪽과 오른쪽을 계속 가리킬 수 있도록하고 있으며 index가 length보다 커지면 return none으로 연결되지 않게 한다. 

        # 3강 실습 1의 연결리스트에서는 노드를 위와 같이 정의하였다. 
        # 그리고 연결리스트에서의 연결은 연결리스크 클래스에서 addToEnd라는 함수로 node를 인자로 받은다음에 연결하였다.

        # class Node:
        #     def __init__(self, val):
        #         self.val = val
        #         self.next = None

        # class LinkedList:
        #     def __init__(self, head): # LinkedList(Node(3))과 같은형태로 인자 head가 노드임. 그래서 self.tail.next를 사용할 수 있음.
        #         self.head = head
        #         self.tail = head
            
        #     def addToEnd(self, node): # LinkedList(Node(3))과 같은형태로 인자 head가 노드임. 그래서 self.tail.next를 사용할 수 있음.
        #         self.tail.next = node
        #         self.tail = node

        # 즉 어떠한 자료구조를 사용하고 싶다면, 연결이 되어야하기에 노드는 값과, 주소를 담는 변수가 필요하고 
        # 주소를 실제로 넣는것은 그 자료구조에 맞게 helper , addToEnd와 같은 메소드를 통해 주소를 넣어주어야한다. 

        # addToEnd와 같이 수동으로 하나하나 넣을 수 있고, 그리고 3장 실습1번 처럼 반복문을 사용해서 넣을 수 있으며
        # helper와 같이 재귀를 이용해 넣을 수 있다. 

    return helper(0)
    # helper(0)은 node를 리턴하는데 이 node에 node.left , node.right의 형태로 다음노드들의 주소가 연결되어있고, 이 주소는 node라는 변수에 담긴다.
    # helper(1) 이 호출될때 node에 새로운 값이 담기지만 그건 상관이 없는것이다. node(0) 이 호출되고 helper(1)을 부른다음에  node에 또 주소정보가 담긴다. 
    # 여담인데 , 이런식으로 주소를 저장할 변수를 하나로 끝내는 코드를 짜는게 진짜 어려운것같다. 
#=================================================================================
# printTree는 입력받은 트리를 bfs방식으로 탐색하여 출력하는 함수이다. 
def printTree(node):

    # return node.val

    # all_lines = []

    # 궁금증 1) node만 받아서 2,3,4,5,6,7을 어떻게 다 추가할 수 있을까? 
    # printTree를 계속 실행해서 값을 추가하도록 해야할것같다 -> 재귀적인 방법 그러나 dfs 임. 


    # all_lines.append(node.val)

    # 궁금증 2)
    # all_lines.append(node.left)
    # all_lines.append(node.right)

    # 여기서 node.left에서 다시 자신의 node.left를 어떻게 부를 수 있을까? 

    # 해결책 # 중요한점
    # printTree를 계속 실행하는게 아니라, 연산이 될 노드를 계속 바꿔주면 된다. 
    # 즉  while문을 통해 연산을 걸고, 노드를 계속 바꿔주는 방식으로 말이다. 

    # thislevel =node
    # while thislevel : # thislevel 이 있으면? 을 이렇게 표현하는게 맞나? 
    #     all_lines.append(thislevel.val)
    #     if thislevel.left : # thislevel.left가 있으면을 이렇게 표현하는게 맞나?
    #         all_lines.append(thislevel.left.val)
    #     if thislevel.right :
    #         all_lines.append(thislevel.right.val)
    #     thislevel = thislevel.left 
            # 그런데 lst[0]에서 lst[1],lst[2]이런식으로 한 층에있는걸 다 봐야하는데.. 
            # 여기서 thislevel = thislevel.left이렇게 넣어버리면 층을 돌지 못하고 깊게 들어가버린다.


    # 따라서 nextlevel 을 어떻게 정의할지를 생각해주어야한다. 
    # 1) nextlevel은 그때그떄 새로만든다. 

    # 2) 노드 하나만 출력하는게 아니라, 한 층을 다같이 출력한다. 출력은 n.value로만 이루어진다.
    # 즉 반복문에서 all_lines.append(thislevel.val), all_lines.append(thislevel.left.val)와 같은 방식으로 append가 여러번 일어나지 않도록 한다.

    # 3) for문을 돌면서 리스트안의 현재 노드가 자식노드를 가지고 있으면 일단 넣어놓기. 
    # 근데 너비우선탐색을 위해 for문을 써야한다. 어떻게 써야한다는 직관적인 이해는 아직 되지 않음. 
    
    all_lines = []
    thislevel = [node]

    while thislevel:
        nextlevel = []
        for n in thislevel:  # 탐색이 한줄로 일어나려면  반복문이 실행되어야한다. 
            # 반복문으로 수행할 문장은 다음의 반복문에 들어올 노드들의 순서를 담는것이다. 
            
            if n.left: 
                nextlevel.append(n.left)
            if n.right: 
                nextlevel.append(n.right)
        
        # all_lines.append(nextlevel)
        # 가 노드로 연결되는 것을 해결하기위해 값을 담는 리스트를 만듦 .
        val_list =[]
        for i in range(len(thislevel)):
            val_list.append(thislevel[i].val)

        all_lines.append(val_list)
    

        thislevel = nextlevel
    
    
    return all_lines

    # 이진트리를 어떻게 큐를이용해서 구현할 수 있나? 감이 안잡힘 

def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    
    print(printTree(node)) # [[1], [2, 3], [4, 5, 6, 7]]

if __name__ == "__main__":
    main()
    