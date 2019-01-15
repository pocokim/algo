# 연결 리스트의 노드. 단일 연결 리스트의 경우입니다.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.val)

# 연결 리스트 클래스. head 와 tail을 가지고 있으며, 가장 뒤에 새로운 노드를 추가하는 addToEnd 함수가 있습니다.
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
    
    def addToEnd(self, node):
        self.tail.next = node
        self.tail = node
        
    def __str__(self):
        node = self.head
        toPrint = []
        while node:
            toPrint.append(str(node.val))
            node = node.next
        return "->".join(toPrint)

# 주어진 배열을 linkedlist로 변환해서 돌려줍니다. 실습 3-1을 참조하세요
def toLinkedList(lst):
    ll = LinkedList(Node(lst[0]))
    for i in range(1, len(lst)):
        ll.addToEnd(Node(lst[i]))

    return ll
    
####################################################################################################################################

def deleteNode(ll, valToDelete):

    # node = ll.head
    # while node:
    #     print(node)
    #     if node.val == valToDelete: # node는 객체 , valToDelete는 int형 변수 서로 비교가 안되는것인가?  -> 가능하다.
    #         print('찾았습니다!')
    #         del node # 이렇게 삭제하는게 아닌듯
    #         break # 오류가 났던 이유 : node를 삭제한뒤에도 노드를 참조하려고 했기때문.
        
    #     node = node.next

    # # 이 코드가 잘못된 이유 : 삭제한다음에, 앞의 노드와 뒤의 노드를 연결하지 않았기때문. 

    # beforeNode = ll.head
    # currNode = beforeNode.next
    # nextNode = currNode.next
    

    # while nextNode :
    #     print(currNode)
    #     if currNode.val == valToDelete:
    #         # print('beforenode'+str(beforeNode.next))
    #         # print('nextnode'+str(nextNode))
    #         # beforeNode.next = nextNode
    #         print('걸렸습니다')
    #         beforeNode,currNode,nextNode = nextNode,nextNode,nextNode.next
    #         print(beforeNode,currNode,nextNode)
        
    #     # else : currNode = nextNode 
    #     else :
    #         beforeNode,currNode,nextNode = currNode,nextNode,nextNode.next # 여기서 beforeNode = currNode이게 잘못된것같음. 
    #         print(beforeNode,currNode,nextNode)
    #         print('안걸렸습니다')

    #     print(currNode)
        
        # 2 8 19 
        # 8 37 4
        # 37 4 5 를 출력해야하는데

        # 2 8 19
        # 8 19 37
        # 37 37 4
        # 37 4 5  로 출력함. 이건 괜찮은데..

        # 8이 beforeNode일때는 beforeNode(8) = nextNode(37) 을 넣어서 19가 연결되지 않도록 했는데
        # 8이 currNode일때는 nextNode인 19와 연결이 되어버리는 문제가 있어서 출력을할때 19를 삭제하지 않고 출력하는것같음.

    # if ll.head.val == valToDelete :
    #     ll.head = ll.head.next
    
    # node = ll.head.next

    
    # while node != ll.tail:
    #     # print(node)
    #     # print(node.next)
    #     # print(node.next.val) node.next 는 노드고, node.next.val은 값인것같다. 따라서 if문으로 비교할때는 next가 아니라 val로 비교를 해야하는것같다.
    #     print('이게 넥스트'+str(node.next))
    #     if node.next.val == valToDelete:

    #         # 1)adddToEnd사용했던 시도 
    #         # ll.addToEnd(node.next.next)

    #         # 2)addToEnd사용 못해서 자체로 만들어봤던시도
    #         # node.tail.next = node.next.next  
    #         # node.tail = node.next.next
    #         # AttributeError: 'Node' object has no attribute 'tail'  
            
    #         # 3) node못써서  linkedlist 써봤던 시도 
    #         # ll.tail.next = node.next.next
    #         # ll.tail = node.next.next
    #         # 새로운 리스트객체를 만들어서 처리하는 방법이외에는 생각이 안남..

    #     node = node.next 

    if ll.head.val == valToDelete:
        ll.head = ll.head.next

    currNode = ll.head
    nextNode = currNode.next

    # 변수 3개안쓰고 2개만써서도 해결할수 있음. 위에서 beforeNode 안쓴것처럼 풀은것.
    while nextNode :
        # print(nextNode)
        if nextNode.val == valToDelete:
            currNode.next = nextNode.next

        # 해설에는 이 코드있는데 굳이 필요한가? nextNode 는 어짜피 while문을 돌면서 none만나면 탈출함.
        # if nextNode == ll.tail
        #     # currNode = ll.tail #ll.tail = currNode 상관없을듯? 
        # break

        nextNode = nextNode.next
        currNode = currNode.next # 이것도 옮겨 주어야했음 .. 이걸하지않으면 2->37->4->5 이렇게 나옴  

        # print(currNode)
        # print(ll)

    

def main():
    nums = [2,8,19,37,4,5]
    ll = toLinkedList(nums)
    print(ll)
    deleteNode(ll, 19)
    print(ll) # 19를 삭제하였으므로, 2->8->37->4->5
    deleteNode(ll, 3)
    print(ll) # 3이 없으므로, 2->8->37->4->5

if __name__ == "__main__":
    main()