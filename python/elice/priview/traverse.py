class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def traverse(rootnode):
  thislevel = [rootnode]
  print('[',end="")
  while thislevel:
    nextlevel = list()
    print('[',end="")
    for n in thislevel:
      print(thislevel)  
      print(n.value,end="")
      if n.left: nextlevel.append(n.left)
      if n.right: nextlevel.append(n.right)
    print(']',end="")
    # print('nextlevel')
    # print(nextlevel)
    thislevel = nextlevel
  print(']',end="")
t = Node(1, Node(2, Node(4, Node(7))), Node(3, Node(5), Node(6)))

traverse(t)