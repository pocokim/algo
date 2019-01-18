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
def printTree(node):
    all_lines = []
    return all_lines

def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    
    print(printTree(node)) # [[1], [2, 3], [4, 5, 6, 7]]

if __name__ == "__main__":
    main()
    