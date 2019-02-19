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

# 노드는 next로 노드와 연결되고 
# 리스트는 head와 tail을 통해 연결된다. 

# 결국 바꿔 주어야하는것은 리스트의 연결이다. 
# 리스트에서 삭제하고자 하는 값을 만나면 
# 19의 앞인 8이 19의 다음인 37에 연결되어야한다. 

# currNode 와 nextNode 를 2개를 설정하여 해결 할 수 있다.


def deleteNode(ll, valToDelete):
    # 리스트를 돌면서 삭제하고자 하는 값을 만나면 삭제
    if ll.head.val == valToDelete:
        ll.head = ll.head.next
    else :
        currNode = ll.head
        nextNode = currNode.next 

        while  nextNode: 
            # 19를 기준으로 8과 37을 연결시켜주어야하므로 8에서 봤을때 19를 찾고, 19의 다음인 37로 8과 연결시켜주는 맥락.currNode를 기준으로 nextNode를 보는것이다. 
            # nextNode가 아니라 currNode로 while문을 돌리면 currNode가 4일때 nextNode.val이 5고 nextNode.next의 값이 존재하지 않기때문에 
            # 근데 while문에 nextNode, currNode가 들어가는게 중요한게 아니라 끝을 어떻게 처리하는지가 더 중요한것같다. 
            if nextNode.val == valToDelete:
                if nextNode == ll.tail : 
                    # ll.tail = currNode # 질문 1
                    # currNode.next = None

                    currNode.next = None
                    ll.tail = currNode 

                    break # 질문 2


                currNode.next = nextNode.next
            
            
            
                
            currNode = currNode.next
            nextNode = nextNode.next
# 배운점 
# 1. break 는 반드시 필요하지는 않다. 이 함수는 valToDelete를 찾아내는 함수이다. 있으면 시간이 더 줄어들어서 사용한다. 
# 2. ll.tail = currNode 와  currNode.next = None 의 위치를 바꿔주는것이 포인트였다. 그런데 이게 왜 차이를 만드는지는 모르겠다. 더 좋은건 알겠지만 .. 반드시 필요한 표현인지는 모르겠음. 

def main():
    nums = [2,8,19,37,4,5]
    ll = toLinkedList(nums)
    print(ll)

    deleteNode(ll, 19)
    print(ll) # 19를 삭제하였으므로, 2->8->37->4->5
    deleteNode(ll, 3)
    print(ll) # 3이 없으므로, 2->8->37->4->5
    deleteNode(ll, 5)
    print(ll) # 3이 없으므로, 2->8->37->4->5

if __name__ == "__main__":
    main()