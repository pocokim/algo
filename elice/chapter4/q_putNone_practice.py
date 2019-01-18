import queue 

q = queue.Queue()
q.put(1)
q.put(None)

print(q.qsize())

# None도 queue에 들어갈 수 있음.