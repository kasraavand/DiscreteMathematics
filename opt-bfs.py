from collections import deque

def bfs(graph, start, target):
    queue = deque()
    queue.append(start)

    def find_path(t, k, start, target, p = deque()):
        if len(t) > 1:
            for (ind, (i, j,),) in enumerate(t):
                if j == k[0]:
                    p.appendleft(j)
                    k = t.pop(ind)
                    return find_path(t, k, start, target, p)

        p.appendleft(start)
        p.append(target)
        return p


    #use generator for large graphs 
    def find_path2(t, s):
        p = (find_path(t, a) for (a, b,) in t if b == s)
        return [s] + next(p, [])



    def ff(queue, temp = set(), visited = {start}, path = []):
        for q in queue:
            visited.add(q)
            for node in graph[q] - (visited | set(queue)):
                temp.add(node)
                path.append((q, node))
                if node == target:
                    return find_path(path, (q, node), start, target)
                visited.add(node)


        return ff(temp, temp=set(), path=path)


    return ff(queue)


g={'A':{'F','G'},
   'B':{'S','F'},
   'C':{'D','E','Z'},
   'D':{'C','S'},
   'E':{'F','C'},
   'F':{'E','B','A'},
   'G':{'A'}, 
   'S':{'B','D'},
   'Z':{'C'}
}

print bfs(g,'A','Z')