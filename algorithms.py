## Algorithms

def calculate_seek(path):
    return sum(abs(path[i] - path[i+1]) for i in range(len(path) - 1))

def fcfs(req, head):
    return [head] + req, calculate_seek([head] + req)

def sstf(req, head):
    path = [head]
    temp_req = req.copy()
    while temp_req:
        closest = min(temp_req, key=lambda x: abs(x - path[-1]))
        path.append(closest)
        temp_req.remove(closest)
    return path, calculate_seek(path)

def scan(req, head, size):
    left = sorted([x for x in req if x < head], reverse=True)
    right = sorted([x for x in req if x >= head])
    path = [head] + right + [size - 1] + left + [0]
    return path, calculate_seek(path)

def cscan(req, head, size):
    left = sorted([x for x in req if x < head])
    right = sorted([x for x in req if x >= head])
    path = [head] + right + [size - 1] + [0] + left
    return path, calculate_seek(path)