# 연결 리스트의 노드. 단일 연결 리스트의 경우입니다.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.val) # print할때 사용하려는거지 ? node(5)를 넣는다고 하면 , 클래스가 들어가는건지? 값이 들어가는건지? (클래스가 들어가고, 표현만 값으로 하는것같다.)

# 연결 리스트 클래스. head 와 tail을 가지고 있으며, 가장 뒤에 새로운 노드를 추가하는 addToEnd 함수가 있습니다.
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
    
    def addToEnd(self, node):
        self.tail.next = node # self.next가 아니라 self.tail.next가 되는이유? 선언하기 나름인데 head와 tail을 선언하고 연결해주기위해서는 tail의 next라고 선언해주어야한다. # 중간연결
        # self.next = node라고 하면, 연결이 되지 않는다. 그거 확인은 아래 __str__에서 가능함
        self.tail = node # 마지막연결 
        
    def __str__(self):
        node = self.head
        toPrint = []
        while node:
            toPrint.append(str(node.val))
            # print(node)
            node = node.next
            # print(node)
        return "->".join(toPrint)

####################################################################################################################################

# 주어진 연결 리스트 ll을 배열로 변환해 봅시다.
# 이때 연결 리스트 LinkedList의 객체가 입력으로 주어진다고 가정합니다.
def toArray(llNode):
    # 처음의 풀이 1 
    # temp =[llNode.head]
    # print(llNode.head)
    # print(temp)   
    # 링크드 리스트를 배열에 넣을때는 객체로 들어가고, 값을 그대로 사용할때는 배열이 아니라 값으로써 사용이 되는듯.

    # temp =[llNode.head]
    # temp2 =[]

    # node = temp[0]
    # while node:
    #     temp2.append(node.val)
    #     node = node.next    
    # return temp2

    # temp2 안쓰고  temp로만은 못하나..?

    # print(type(llNode))
    # a  = llNode.split('->')
    # print(a)
    
    # 개선된 풀이 2 
    # print(type(llNode.head))
    # llNode는 리스트이지만, llNode.head는 노드임.
    # 배열에 넣을때는 왜 값이 아니라 클래스로 담기는지는 모르곘음... 
    
    node = llNode.head
    temp = []
    while node:
        temp.append(node.val)
        node = node.next    
    return temp



# 주어진 배열을 연결 리스트로 변환 해 봅시다.
def toLinkedList(lst):
    LL=LinkedList(Node(lst[0]))
    for i in range(1,len(lst)):
        LL.addToEnd(Node(lst[i]))
        
    return LL

def example():
    ## Linkedlist 클래스와 Node 클래스를 사용하는 예시입니다.
    ll = LinkedList(Node(3))
    ll.addToEnd(Node(4))
    ll.addToEnd(Node(8))
    print(ll)
    print(ll.head)
    print(ll.tail)

def main():
    example()
    nums = [2,8,19,37,4,5]
    ll = toLinkedList(nums)
    print(ll)
    lst = toArray(ll)
    print(lst)

if __name__ == "__main__":
    main()
