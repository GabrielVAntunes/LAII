def next_moves(adj, pos):
    adj[pos] = [(pos[0] + 2, pos[1] + 1 ), (pos[0] + 2, pos[1] - 1),(pos[0] + 1, pos[1] - 2),(pos[0] - 1,pos[1] - 2),
                (pos[0] - 2,pos[1] - 1),(pos[0] - 2, pos[1] + 1),(pos[0] - 1,pos[1] + 2),(pos[0] + 1, pos[1] + 2)]
    return adj
    
def bfs(adj,o,dest):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        adj = (next_moves(adj, v))
        if v == dest:
            break
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
                
    return pai

def saltos(o,d):
    
    if o == d:
        return 0
        
    orig = o
    dest = d
    
    adj = {}

    pai = bfs(adj,orig, dest)
    resp = 0
    
    while (dest != orig):
        resp +=1
        dest = pai[dest]
        
    return resp

# 100 %