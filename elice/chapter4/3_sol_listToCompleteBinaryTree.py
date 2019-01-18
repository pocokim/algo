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

        
    return helper(0)
    
def printTree(node):

    # 이진트리를 어떻게 큐를이용해서 구현할 수 있나? 감이 안잡힘 

    all_lines = []
    line =[]

    q = queue.Queue()
    q.put(node)
    q.put(Node(-1)) # -1을 통해 각 깊이를 구별하기 위함.

    while q.qsize() > 0 : # q에 들어온 데이터가 있을때 
        print(q.qsize())
        node = q.get()

        # not node 라는건 node가 없다는건데, 어떻게 그럴수있나? 
        # node 에 none 이 있으면 이라는뜻인가? 

        if not node : #node == None이라는 뜻인가? 
            continue
        # q.get()으로 가져온 노드가 존재 하지않는다면  q의 사이즈를 확인하는 조건문으로 왜 들어감? 
        # AttributeError: 'NoneType' object has no attribute 'val'

        else: # q.get()으로 가져온 노드가 존재한다면 
            if node.val == -1 :# 근데 그게 -1이라면 새 리스트 만들어야함. -- > -1을 만나면 그전에 line에 있던거를 all_line에 넣고, 새 층을 만들어준다. 
                if q.qsize() >0 : # 이걸 굳이 왜 또 해야함? 
                    all_lines.append(line) 
                    line =[]
                    q.put(Node(-1))
            else :
                line.append(node.val)
                q.put(node.left)
                q.put(node.right)
                # node.left가 존재하지 않을 경우에 q.put(None)이 들어가나 
                # 아니면 아예 안들어가나? - > None이 들어간다. 

    return all_lines          

# 큐를 왜 쓸까했는데, q에 같은 레벨의 데이터들을 넣고 while문으로 q의 사이즈를 본다.         

def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    
    print(printTree(node)) # [[1], [2, 3], [4, 5, 6, 7]]

if __name__ == "__main__":
    main()
    

# 배운점 1) 
# 큐가 순서대로  fifo를 처리하기에 순서대로 무언가를 처리하고 싶다면 반복문이나 큐를 생각하는것이 일반적임
# 배운점 2) 
# 조건문의 논리연산은 True False 인데, 1은 true , 0은 false, none도 false를 의미한다.
# 배운점 3) 노드가 없으면
# 노드가 없으면 이라는 뜻은 node = q.get()으로 분명 가져왔는데 없다고 말할수있냐? 고 생각할 수 있지만
# none을 가져오는건 없다를 가져오는것이어서 가져오는게 아님. 