
# 실습 3-3과 정의가 약간 바뀌었습니다. 유의하세요.
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

# head node가 주어졌을 때 해당 링크드리스트를 문자열로 변환해 주는 함수입니다.
def linkedListToStr(node):
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

# head 노드가 주어졌을 때, 해당 링크드 리스트를 뒤집은 후 뒤집힌 링크드 리스트의 헤드를 반환하는 함수를 구현 해 보세요.
def reverseLinkedList(head):
    # 풀이 1  배열을 만들고, 배열을 뒤집은 다음에 그 배열을 리스트로 만들고 그 헤드를 리턴하는 방식으로 해결 
    # 연결리스트 자료구조가 어려워서 그냥 야매로 쉬운 배열을 이용해서 풀어봄.
    node = head
    temp =[]
    while node:
        temp.append(node.val)
        node = node.next
    temp.reverse()

    return toLinkedList(temp).head



    # return head

def main():
    nums = [2,8,19,37,4,5]
    # print(type(toLinkedList(nums)))
    # print(type(toLinkedList(nums).head))

    head_node = toLinkedList(nums).head
    # head_node에는 2~ 5까지의 연결이 이미 담겨져있음.
    # 즉 reverseLinkedList도 전체연결을 다 바꿔야한다는뜻임.
        
    print(linkedListToStr(head_node)) # 2->8->19->37->4->5


    reversed_head_node = reverseLinkedList(head_node)
    print(linkedListToStr(reversed_head_node)) # 5->4->37->19->8->2

if __name__ == "__main__":
    main()